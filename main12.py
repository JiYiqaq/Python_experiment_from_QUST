import random


class Player:
    def __init__(self, score=0):
        self.name = "玩家"
        self.score = score

    def player_action(self, choice):
        if choice == 1:
            print(f"{self.name}出石头")
        elif choice == 2:
            print(f"{self.name}出剪刀")
        elif choice == 3:
            print(f"{self.name}出布")


class Computer:
    def __init__(self, score=0):
        self.cname = "电脑"
        self.score = score

    def computer_action(self, choice):
        if choice == 1:
            print(f"{self.cname}出石头")
        elif choice == 2:
            print(f"{self.cname}出剪刀")
        elif choice == 3:
            print(f"{self.cname}出布")


class Game:
    count = 0

    def __init__(self):
        self.player = Player()
        self.computer = Computer()

    def show_result(self):
        print(f"本次游戏共进行了{self.count}局")
        print(f"{self.player.name}的得分是{self.player.score}")
        print(f"{self.computer.cname}的得分是{self.computer.score}")

        if self.player.score > self.computer.score:
            print(f"恭喜您获胜！")
        elif self.player.score < self.computer.score:
            print(f"很遗憾，您输了！")
        else:
            print("平局！")

    def play(self):
        answer = input("是否开始游戏？（y/n）").lower()

        if answer != 'y':
            print("游戏结束！")
            return

        self.count = int(input("请输入游戏的局数："))

        for i in range(self.count):
            print(f"\n第{i + 1}局开始：")

            player_choice = int(input("请出拳（1-石头，2-剪刀，3-布）："))
            computer_choice = random.randint(1, 3)

            self.player.player_action(player_choice)
            self.computer.computer_action(computer_choice)

            if player_choice == computer_choice:
                print("平局！")
            elif (player_choice == 1 and computer_choice == 2) or \
                    (player_choice == 2 and computer_choice == 3) or \
                    (player_choice == 3 and computer_choice == 1):
                print("恭喜您获胜！")
                self.player.score += 1
            else:
                print("很遗憾，您输了！")
                self.computer.score += 1

        self.show_result()


def main():
    game = Game()
    game.play()


if __name__ == '__main__':
    main()
