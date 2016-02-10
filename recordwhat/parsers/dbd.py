"""
Simple EPICS DBD parser that uses pyparsing

NOTE: it would have been easier just to write a custom parser for the dbd files -- this
      was just to try out pyparsing, really.

Grabs all record information from dbd files and dumps them out into a text file
with one field per line along with its associated properties

Though it parses all of the dbds in base and synapps, it probably won't parse everything.

TODO: breaktable syntax
"""

from __future__ import print_function
import os
import sys
import re
from pyparsing import *

LPAR,RPAR,LBRACK,RBRACK,LBRACE,RBRACE,SEMI,COMMA = [Suppress(c) for c in r"()[]{};,"]
PERCENT = Regex(r'%')
RECORDTYPE = Keyword("recordtype")
DQUOTE = Regex(r'"')
SQUOTE = Regex(r"'")

integer = Regex(r"[+-]?\d+")
char = Regex(r"'.'")
float_ = Regex(r'\d+(\.\d*)?([eE]\d+)?')
string_ = quotedString
c_identifier = Word(alphas+"_", alphanums+"_") # valid C identifier
PV = Word(alphanums + '_-:.[]<>;')
RTYP = Word(alphanums)
MENU_NAME = Word(alphanums + '_')
c_declaration = SkipTo(LineEnd(), include=True)

PATH = Keyword('path')
ADDPATH = Keyword('addpath')
INCLUDE = Keyword('include')
MENU = Keyword('menu')
CHOICE = Keyword('choice')
RECORDTYPE = Keyword('recordtype')
FIELD = Keyword('field')
DEVICE = Keyword('device')
DRIVER = Keyword('driver')
REGISTRAR = Keyword('registrar')
FUNCTION = Keyword('function')
VARIABLE = Keyword('variable')
BREAKTABLE = Keyword('breaktable')
RECORD = Keyword('record')
GRECORD = Keyword('grecord') # TODO not handled
INFO = Keyword('info')
ALIAS = Keyword('alias')

ASL = Keyword('asl')
INITIAL = Keyword('initial')
PROMPTGROUP = Keyword('promptgroup')
PROMPT = Keyword('prompt')
SPECIAL = Keyword('special')
PP = Keyword('pp')
INTEREST = Keyword('interest')
BASE = Keyword('base')
SIZE = Keyword('size')
EXTRA = Keyword('extra')
MENU = Keyword('menu')

FIELD_NAME = c_identifier
DBF_STRING = Keyword('DBF_STRING')
DBF_CHAR = Keyword('DBF_CHAR')
DBF_UCHAR = Keyword('DBF_UCHAR')
DBF_SHORT = Keyword('DBF_SHORT')
DBF_USHORT = Keyword('DBF_USHORT')
DBF_LONG = Keyword('DBF_LONG')
DBF_ULONG = Keyword('DBF_ULONG')
DBF_FLOAT = Keyword('DBF_FLOAT')
DBF_DOUBLE = Keyword('DBF_DOUBLE')
DBF_ENUM = Keyword('DBF_ENUM')
DBF_MENU = Keyword('DBF_MENU')
DBF_DEVICE = Keyword('DBF_DEVICE')
DBF_INLINK = Keyword('DBF_INLINK')
DBF_OUTLINK = Keyword('DBF_OUTLINK')
DBF_FWDLINK = Keyword('DBF_FWDLINK')
DBF_NOACCESS = Keyword('DBF_NOACCESS')

ASL0 = Keyword('ASL0')
ASL1 = Keyword('ASL1')
ASLS = Group(ASL0 | ASL1)

GUI_COMMON = Keyword('GUI_COMMON')
GUI_ALARMS = Keyword('GUI_ALARMS')
GUI_BITS1 = Keyword('GUI_BITS1')
GUI_BITS2 = Keyword('GUI_BITS2')
GUI_CALC = Keyword('GUI_CALC')
GUI_CLOCK = Keyword('GUI_CLOCK')
GUI_COMPRESS = Keyword('GUI_COMPRESS')
GUI_CONVERT = Keyword('GUI_CONVERT')
GUI_DISPLAY = Keyword('GUI_DISPLAY')
GUI_HIST = Keyword('GUI_HIST')
GUI_INPUTS = Keyword('GUI_INPUTS')
GUI_LINKS = Keyword('GUI_LINKS')
GUI_MBB = Keyword('GUI_MBB')
GUI_MOTOR = Keyword('GUI_MOTOR')
GUI_OUTPUT = Keyword('GUI_OUTPUT')
GUI_PID = Keyword('GUI_PID')
GUI_PULSE = Keyword('GUI_PULSE')
GUI_SELECT = Keyword('GUI_SELECT')
GUI_SEQ1 = Keyword('GUI_SEQ1')
GUI_SEQ2 = Keyword('GUI_SEQ2')
GUI_SEQ3 = Keyword('GUI_SEQ3')
GUI_SUB = Keyword('GUI_SUB')
GUI_TIMER = Keyword('GUI_TIMER')
GUI_WAVE = Keyword('GUI_WAVE')
GUI_SCAN = Keyword('GUI_SCAN')

spc_int_greater_102 = integer # TODO
SPC_NOMOD = Keyword('SPC_NOMOD')
SPC_SCAN = Keyword('SPC_SCAN')
SPC_ALARMACK = Keyword('SPC_ALARMACK')
SPC_AS = Keyword('SPC_AS')
SPC_DBADDR = Keyword('SPC_DBADDR')
SPC_MOD = Keyword('SPC_MOD')
SPC_RESET = Keyword('SPC_RESET')
SPC_LINCONV = Keyword('SPC_LINCONV')
SPC_CALC = Keyword('SPC_CALC')

CONSTANT = Keyword('CONSTANT')
PV_LINK = Keyword('PV_LINK')
VME_IO = Keyword('VME_IO')
CAMAC_IO = Keyword('CAMAC_IO')
AB_IO = Keyword('AB_IO')
GPIB_IO = Keyword('GPIB_IO')
BITBUS_IO = Keyword('BITBUS_IO')
INST_IO = Keyword('INST_IO')
BBGPIB_IO = Keyword('BBGPIB_IO')
RF_IO = Keyword('RF_IO')
VXI_IO = Keyword('VXI_IO')

NO = Keyword('NO')
YES = Keyword('YES')
TRUE = Keyword('TRUE')
FALSE = Keyword('FALSE')

DECIMAL = Keyword('DECIMAL')
HEX = Keyword('HEX')

keyword = Group(RECORDTYPE | DEVICE | DRIVER | REGISTRAR | VARIABLE | BREAKTABLE)
gui_group = Group(GUI_COMMON | GUI_ALARMS | GUI_BITS1 | GUI_BITS2 | GUI_CALC | GUI_CLOCK | GUI_COMPRESS | GUI_CONVERT | GUI_DISPLAY | GUI_HIST | GUI_INPUTS | GUI_LINKS | GUI_MBB | GUI_MOTOR | GUI_OUTPUT | GUI_PID | GUI_PULSE | GUI_SELECT | GUI_SEQ1 | GUI_SEQ2 | GUI_SEQ3 | GUI_SUB | GUI_TIMER | GUI_WAVE | GUI_SCAN)
field_type = Group(DBF_STRING | DBF_CHAR | DBF_UCHAR | DBF_SHORT | DBF_USHORT | DBF_LONG | DBF_ULONG | DBF_FLOAT | DBF_DOUBLE | DBF_ENUM | DBF_MENU | DBF_DEVICE | DBF_INLINK | DBF_OUTLINK | DBF_FWDLINK | DBF_NOACCESS)
rules = Group(ASL | INITIAL | PROMPTGROUP | PROMPT | SPECIAL | PP | INTEREST | BASE | SIZE | EXTRA | MENU)
special_value = Group(SPC_NOMOD | SPC_SCAN | SPC_ALARMACK | SPC_AS | SPC_DBADDR | SPC_MOD | SPC_RESET | SPC_LINCONV | SPC_CALC | spc_int_greater_102)
pp_value = Group(NO | YES | TRUE | FALSE)
base_type = Group(DECIMAL | HEX)
link_type = Group(CONSTANT | PV_LINK | VME_IO | CAMAC_IO | AB_IO | GPIB_IO | BITBUS_IO | INST_IO | BBGPIB_IO | RF_IO | VXI_IO)
dset_name = c_identifier

def brace_group(name, entries, types=None):
    if types is not None:
        # name(type) { entries }
        ret = name + LPAR
        for type_ in types[:-1]:
            ret += type_
            ret += COMMA
        ret += types[-1] + RPAR
        return Group(ret + LBRACE + ZeroOrMore(entries) + RBRACE)
    else:
        # name { entries }
        ret = name

    return Group(ret + LBRACE + ZeroOrMore(entries) + RBRACE)

def paren_group(name, *entries):
    # name(entry1, entry2, ...)
    ret = name + LPAR
    # TODO sum() does not work
    for entry in entries[:-1]:
        ret += entry
        ret += COMMA
    ret += entries[-1]
    ret += RPAR
    return Group(ret)
#types = [Keyword(k) for k in ('prompt', 'field', 'recordtype', 'promptgroup', 'asl', 'pp')]
#TYPE = Group(reduce(lambda x, y: x | y, types))

def optionally_quoted(token):
    return Group((DQUOTE + token + DQUOTE) | token)

# -- fields --
asl = paren_group(ASL, ASLS)
initial = paren_group(INITIAL, Group(quotedString | float_))
promptgroup = paren_group(PROMPTGROUP, optionally_quoted(gui_group))
prompt = paren_group(PROMPT, quotedString)
special = paren_group(SPECIAL, optionally_quoted(special_value))
pp = paren_group(PP, optionally_quoted(pp_value))
interest = paren_group(INTEREST, optionally_quoted(integer))
base = paren_group(BASE, base_type)
size = paren_group(SIZE, optionally_quoted(integer))
extra = paren_group(EXTRA, quotedString)
field_menu = paren_group(MENU, optionally_quoted(MENU_NAME))

# -- record c code inclusion --
c_code = Group(PERCENT + Optional(c_declaration))

# -- record subgroups
field_rule = Group(asl | initial | promptgroup | prompt | special | pp | interest | base | size | extra | field_menu)
field = brace_group(FIELD, field_rule, types=(FIELD_NAME, field_type))
choice = paren_group(CHOICE, c_identifier, quotedString)
menu = brace_group(MENU, choice, types=(c_identifier, ))

include = INCLUDE + quotedString

# -- the record itself
record = brace_group(RECORDTYPE, field | include | c_code, types=(RTYP, ))

# -- all top-level .dbd entries
device_line = paren_group(DEVICE, RTYP, link_type, dset_name, quotedString)
driver_line = paren_group(DRIVER, c_identifier)
registrar_line = paren_group(REGISTRAR, c_identifier)
variable_line = paren_group(VARIABLE, c_identifier, Optional(c_identifier, default='int'))
top_level = Group(record | menu | device_line | driver_line | registrar_line | variable_line)
dbd = ZeroOrMore(top_level)
dbd.ignore(pythonStyleComment)

# -- include files (supported only for including additional fields)
dbd_include = ZeroOrMore(field | include | c_code)
dbd_include.ignore(pythonStyleComment)

def iter_results(info):
    check = [info]
    while check:
        c = check.pop(0)
        if c:
            if isinstance(c[0], str):
                yield c
            else:
                for other in c:
                    if isinstance(other, list):
                        check.append(other)

import pprint
record_info = {}
def parse_rule(rule):
    if isinstance(rule[1], list):
        return rule[0], rule[1][0]
    return rule

def parse_field(info):
    ret = {}
    ret['name'] = info[1]
    ret['type'] = info[2][0]

    for rule in info[3:]:
        rule = rule[0]
        #print('rule', rule)
        name, value = parse_rule(rule)
        ret[name] = value
    return ret

def parse_record(info):
    ret = { 'fields' : {}}
    ret['type'] = info[1]

    for i, line in enumerate(info):
        if line[0] == 'field':
            field_name = line[1]
            ret['fields'][field_name] = parse_field(line)

    return ret

def parse_includes(line):
    ret = []
    while 'include' in line:
        i = line.index('include')
        include_file = line[i + 1].strip('"')
        print('include file', include_file)
        dbd_incl = parse_dbd_file(include_file, include_file=True)

        line[i] = 'include_done'
        line.extend(dbd_incl)

record_info = {}
def get_rtypes(data):
    #pprint.pprint(data.asList())
    for line in iter_results(data):
        if line[0] == 'recordtype':
            if 'include' in line:
                print('parsed include:')
                parse_includes(line)
                # data updated, inefficiently re-run get_rtypes
                print('reparsing due to include')
                return get_rtypes(data)

            print('found record', line)
            record_type = line[1]
            record_info[record_type] = parse_record(line)

    print('done')

def find_file(fn):
    if not os.path.exists(fn):
        if os.path.exists(os.path.join(DBD_PATH, fn)):
            fn = os.path.join(DBD_PATH, fn)
    return fn

def fix_includes(fn, text):
    while True:
        m = re.search('^(\s*include\s*"(.*)".*)$', text, flags=re.MULTILINE)
        if m is None:
            break

        full_line = m.groups()[0]
        include_file = m.groups()[1]
        print('inserting include file', include_file)
        insert_text = open(find_file(include_file), 'rt').read()
        text = text.replace(full_line, insert_text)

    #open('post_include_%s.dbd' % fn, 'wt').write(text)
    return text

def parse_dbd_file(fn, include_file=False):
    text = open(find_file(fn), 'rt').read()
    text = fix_includes(fn, text)
    try:
        if include_file:
            parsed = dbd_include.parseString(text, parseAll=True)
        else:
            parsed = dbd.parseString(text, parseAll=True)
    except ParseException as ex:
        print(ex.line)
        print(' ' * (ex.column - 1) + "^")
        print(ex)
        return None
    else:
        return parsed.asList()

DBD_PATH = '/usr/lib/epics/dbd'
#rec = get_rtypes(parse_dbd_file('aiRecord.dbd'))
#assert('FLNK' in rec['ai']['fields'])
#pprint.pprint(rec['ai'])

if 0:
    get_rtypes(parse_dbd_file('post_include_busyRecord.dbd.dbd'))
    sys.exit(0)


for fn in os.listdir(DBD_PATH):
    if fn.endswith('.dbd') and 'Record' in fn:
        print('-------------%s--------------' % fn)
        get_rtypes(parse_dbd_file(fn))

columns = ['field', 'type', 'asl', 'initial', 'promptgroup', 'prompt', 'special', 'pp', 'interest', 'base', 'size', 'extra', 'menu']
path = 'output'
for rtype, info in record_info.items():
    with open(os.path.join(path, '%s.txt' % (rtype, )), 'wt') as f:
        print('\t'.join(columns), file=f)
        fields = info['fields']
        for name, field in sorted(fields.items()):
            row = [field[col] if col in field else ''
                   for col in columns]
            row[0] = name
            # Adding the optionally_quoted onto the above put those into a separate list
            # -- I'm tired of modifying the above, so just fix it up here:
            for i, entry in enumerate(row):
                while isinstance(entry, list):
                    row[i] = entry[0]
                    entry = row[i]

            print('\t'.join(row), file=f)
