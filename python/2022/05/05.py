#!/usr/bin/env python3
import re

stacks1 = []
stacks2 = []

with open('input') as inp:
    for line in inp.readlines():
        # line = line.strip()
        if line == '' or re.compile(r'\d').search(line) and 'from' not in line:  # this is ugly...
            continue

        re_stackline = re.compile(r'(   |\[\w\])(?: |$)')  # nothing or crate, use findall to get all crates, second group to catch many spaces, but does not capture them
        re_action = re.compile(r'move (\d+) from (\d+) to (\d+)$')

        m_stackline = re_stackline.findall(line)
        m_action = re_action.match(line)

        if m_stackline:
            if stacks1 == [] and stacks2 == []:  # stacks1 and 2 are always [] at the start
                stacks1 = [[] for _ in range(len(m_stackline))]
                stacks2 = [[] for _ in range(len(m_stackline))]

            for number, item in enumerate(m_stackline):
                if item != '   ':
                    stacks1[number].append(item.replace('[', '').replace(']', ''))
                    stacks2[number].append(item.replace('[', '').replace(']', ''))

        elif m_action: # actions follow after initializing the crates, so execute them right away...
            count, start, end = m_action.groups()
            count, start, end = int(count), int(start)-1, int(end)-1
            stacks1[end] = list(reversed(stacks1[start][:count])) + stacks1[end]
            stacks2[end] = list(stacks2[start][:count]) + stacks2[end]
            del stacks1[start][:count]
            del stacks2[start][:count]
            

        else:
            print(f'Line did not match! "{line}"')


    print(''.join([x[0] for x in stacks1]))
    print(''.join([x[0] for x in stacks2]))

        
