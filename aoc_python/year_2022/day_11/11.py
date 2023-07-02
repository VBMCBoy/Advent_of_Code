#!/usr/bin/env python3
from functools import cache
import re
from math import prod, lcm
from copy import deepcopy

class Monkey:
    def __init__(self) -> None:
        self.items = []
        self.operation = lambda x: x
        self.div_test = 1
        self.true_target = 0
        self.false_target = 0
        self.inspect_count = 0

    def inspect(self, part1: bool, mod_value=1) -> None:
        # print(f'Monkey inspects an item with a worry level of {self.items[0]}.')
        self.items[0] = self.operation(self.items[0])
        # print(f'Worry level has been modified to {self.items[0]}')
        if part1:
            self.items[0] //= 3
            # print(f'Monkey gets bored with item. Worry level is divided by 3 to {self.items[0]}.')
        else:
            self.items[0] %= mod_value
        self.inspect_count += 1

    def get_target(self) -> int:
        if self.items[0] % self.div_test == 0:
            # print(f'Current worry level is divisible by {self.div_test}.')
            # print(f'Item with worry level {self.items[0]} is thrown to monkey {self.true_target}')
            return self.true_target
        else:
            # print(f'Current worry level is not divisible by {self.div_test}.')
            # print(f'Item with worry level {self.items[0]} is thrown to monkey {self.false_target}')
            return self.false_target

    def __str__(self) -> str:
        return(f'''
        Monkey:
          Starting items: {self.items}
          Operation: {self.operation}
          Test: divisible by {self.div_test}
            If true: throw to monkey {self.true_target}
            If false: throw to monkey {self.false_target}
        ''')

monkeys = []
monkey_backup = []
div_values = []

with open('input') as inp:
    for line in inp.readlines():

        # PARSING
        line = line.strip()
        if line == '':
            continue
        if line.startswith('Monkey'):
            monkeys.append(Monkey())
        elif line.startswith('Starting items: '):
            monkeys[-1].items = [int(i) for i in line.replace('Starting items: ', '').replace(' ', '').split(',')]
        elif line.startswith('Operation: '):
            line = line.replace('Operation: new = ', '')
            line = line.split(' ')
            if line[1] == '*':
                if line[2] != 'old':
                    x = int(line[2])
                    monkeys[-1].operation = lambda item, x=x: item*x
                else:
                    monkeys[-1].operation = lambda item: item*item
            elif line[1] == '+':
                if line[2] != 'old':
                    x = int(line[2])
                    monkeys[-1].operation = lambda item, x=x: item+x
                else:
                    monkeys[-1].operation = lambda item: item+item
            else:
                raise ValueError(line)

        elif line.startswith('Test: divisible by '):
            monkeys[-1].div_test = int(line.replace('Test: divisible by ', ''))
            div_values.append(monkeys[-1].div_test)
        elif line.startswith('If true:'):
            monkeys[-1].true_target = int(line.replace('If true: throw to monkey ', ''))
        elif line.startswith('If false:'):
            monkeys[-1].false_target = int(line.replace('If false: throw to monkey ', ''))


    monkey_backup = deepcopy(monkeys)
    for part1, MAX_ROUNDS in [(True, 20), (False, 10000)]:
        # EXECUTION
        monkeys = deepcopy(monkey_backup)
        for i in range(MAX_ROUNDS):
            for monkey in monkeys:
                while monkey.items:
                    # inspect
                    monkey.inspect(part1=part1, mod_value=lcm(*div_values))
                    # get target
                    target = monkey.get_target()
                    monkeys[target].items.append(monkey.items.pop(0))

        if part1:
            print('Part 1:', prod(sorted([monkey.inspect_count for monkey in monkeys])[-2:]))
        else:
            print('Part 2:', prod(sorted([monkey.inspect_count for monkey in monkeys])[-2:]))

