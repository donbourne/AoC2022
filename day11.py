
monkeys = list()

class Monkey:
    test_factor_lcm = 1

    def __init__(self, item_worry_levels, inspection_action, inspection_factor, test_factor, true_monkey, false_monkey, boredom_divisor):

        self.item_worry_levels = item_worry_levels
        self.inspection_action = inspection_action
        self.inspection_factor = inspection_factor
        self.boredom_divisor = boredom_divisor
        self.test_factor = test_factor
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.num_inspects = 0

    def report(self):
        pass
        # print(f'item_worry_levels: {self.item_worry_levels} inspections:{self.num_inspects}')

    def shrink_worry(worry_level):
        if worry_level > Monkey.test_factor_lcm:
            return worry_level % Monkey.test_factor_lcm
        return worry_level

    def action(self):
        while len(self.item_worry_levels) > 0:
            self.num_inspects += 1
            new_worry_level = item_worry_level = self.item_worry_levels.pop(0)
            if self.inspection_action == "*":
                if self.inspection_factor.isdigit():
                    new_worry_level *= int(self.inspection_factor)
                    new_worry_level = Monkey.shrink_worry(new_worry_level)
                else:
                    new_worry_level *= new_worry_level
                    new_worry_level = Monkey.shrink_worry(new_worry_level)
            elif self.inspection_action == "/":
                if self.inspection_factor.isdigit():
                    new_worry_level /= int(self.inspection_factor)
                else:
                    new_worry_level /= new_worry_level
            elif self.inspection_action == "-":
                if self.inspection_factor.isdigit():
                    new_worry_level -= int(self.inspection_factor)
                else:
                    new_worry_level -= new_worry_level
            elif self.inspection_action == "+":
                if self.inspection_factor.isdigit():
                    new_worry_level += int(self.inspection_factor)
                else:
                    new_worry_level += new_worry_level
            else:
                raise f'unrecognized operation {self.inspection_action}'

            new_worry_level /= self.boredom_divisor
            new_worry_level = int(new_worry_level)
            if new_worry_level / self.test_factor == int(new_worry_level / self.test_factor):
                next_monkey = self.true_monkey
            else:
                next_monkey = self.false_monkey
            monkeys[next_monkey].item_worry_levels.append(new_worry_level)


def go(lines, rounds, boredom_divisor):
    Monkey.test_factor_lcm = 1

    for line in lines:
        line = line.strip()
        if line == "":
            pass
        elif line.startswith("Monkey"):
            pass
        elif line.startswith("Starting"):
            item_worry_levels_str = line.replace("Starting items: ", "").replace(",", "").split(" ")
            item_worry_levels = list()
            for i in item_worry_levels_str:
                item_worry_levels.append(int(i))
            # print(item_worry_levels)
        elif line.startswith("Operation"):
            inspection_action, inspection_factor = line.replace("Operation: new = old ", "").split(" ")
            i = ""
            # print(inspection_action, inspection_factor)
        elif line.startswith("Test"):
            test_factor = int(line.replace("Test: divisible by ", ""))
            Monkey.test_factor_lcm *= test_factor
            # print(f'test_factor_lcm: {Monkey.test_factor_lcm}')
        elif line.startswith("If true"):
            true_monkey = int(line.replace("If true: throw to monkey ", ""))
        elif line.startswith("If false"):
            false_monkey = int(line.replace("If false: throw to monkey ", ""))
            # print(test_factor, true_monkey, false_monkey)
            monkey = Monkey(item_worry_levels, inspection_action, inspection_factor, test_factor, true_monkey, false_monkey, boredom_divisor)
            monkeys.append(monkey)
        else:
            print(f'unrecognized: {line}.')

    for i in range(rounds):
        for monkey in monkeys:
            monkey.action()
        # for i, monkey in enumerate(monkeys):
        #     print(f'worry levels{i}: {monkey.item_worry_levels}')

    monkey_inspects = list()
    for monkey in monkeys:
        monkey.report()
        monkey_inspects.append(monkey.num_inspects)

    monkey_inspects.sort(reverse=True)
    print(f'after {rounds} rounds: {monkey_inspects}, monkey_business: {monkey_inspects[0] * monkey_inspects[1]}')

    monkeys.clear()


with open("day11.txt", "rt") as f:
    lines = f.readlines()

# problem 1
go(lines, 20, 3)

# problem 2
go(lines, 10000, 1)