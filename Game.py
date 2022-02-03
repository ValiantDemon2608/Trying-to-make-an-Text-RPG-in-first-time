import random as r

count = 0
hp = 0
coins = 0
damage = 0

def printParameters():
    print("У тебя {0} жизней, {1} урона и {2} монет.".format(hp, damage, coins))

def printHp():
    print("У тебя", hp, "жизней.")

def printCoins():
    print("У тебя", coins, "монет.")

def printDamage():
    print("У тебя", damage, "урона.")

def meetShop():
    global hp
    global damage
    global coins

    def buy(cost):
        global coins
        if coins >= cost:
            coins -= cost
            printCoins()
            return True
        print("У тебя маловато монет!")
        return False

    weaponLvl = r.randint(1, 3)
    weaponDmg = r.randint(1, 5) * weaponLvl
    weapons = ["AK-47", "Iron Sword", "Showel", "Flower", "Bow", "Fish"]
    weaponRarities = ["Spoiled", "Rare", "Legendary"]
    weaponRarity = weaponRarities[weaponLvl - 1]
    weaponCost = r.randint(3, 10) * weaponLvl
    weapon = r.choice(weapons)

    oneHpCost = 5
    threeHpCost = 12

    print("На пути тебе встретился торговец!")
    printParameters()
    
    while input("Что ты будешь делать (зайти/уйти): ").lower() == "зайти":
        print("1) Одна единица здоровья -", oneHpCost, "монет;")
        print("2) Три единицы здоровья -", threeHpCost, "монет;")
        print("3) {0} {1} - {2} монет".format(weaponRarity, weapon, weaponCost))

        choice = input("Что хочешь приобрести: ")
        if choice == "1":
            if buy(oneHpCost):
                hp += 1
                printHp()
        elif choice == "2":
            if buy(threeHpCost):
                hp += 3
                printHp()
        elif choice == "3":
            if buy(weaponCost):
                damage = weaponDmg
                printDamage()
        else:
            print("Я такое не продаю.")

def meetMonster():
    global hp
    global coins

    monsterLvl = r.randint(1, 3)
    monsterHp = monsterLvl
    monsterDmg = monsterLvl * 2 - 1
    monsters = ["Таракан", "Клоп", "Сын маминой подруги", "Нищий", "Демон"]

    monster = r.choice(monsters)

    print("Ты набрел на монстра - {0}, у него {1} уровень, {2} жизней и {3} урона.".format(monster, monsterLvl, monsterHp, monsterDmg))
    printParameters()

    while monsterHp > 0:
        choice = input("Что будешь делать (атака/бег): ").lower()

        if choice == "атака":
            monsterHp -= damage
            print("Ты атаковал монстра и у него осталось", monsterHp, "жизней.")
        elif choice == "бег":
            chance = r.randint(0, monsterLvl)
            if chance == 0:
                print("Тебе удалось сбежать с поля боя!")
                break
            else:
                print("Монстр оказался чересчур сильным и догнал тебя...")
        else:
            continue

        if monsterHp > 0:
            hp -= monsterDmg
            print("Монстр атаковал и у тебя осталось", hp, "жизней.")
        
        if hp <= 0:
            break
    else:
        loot = r.randint(0, 2) + monsterLvl
        coins += loot
        print("Тебе удалось одолеть монстра, за что ты получил", loot, "монет.")
        printCoins()

def Robert():
    global hp
    global damage
    global coins
    input("Ты встретил своего давнего друга Роберта! Хочешь поболтать с ним? (да/нет): ").lower() == "да"
    input("Приветствую тебя Друг, не серчай если попрошу у тебя об одной просьбе? (да/нет): ").lower() == "да"
    quest = r.randint(1,4)
    if quest == 1:
        print("Мне тут на днях доставили много трудностей Клопы. Сможешь их убить для меня? (да/нет): ").lower() == "да"
    elif quest == 2:
        print("Мне тут на днях доставили много трудностей Тараканы. Сможешь их убить для меня? (да/нет): ").lower() == "да"
    elif quest == 3:
        print("Мне тут на днях доставили много трудностей Клопы. Сможешь их убить для меня? (да/нет): ").lower() == "да"
    else:
        print("Я передумал!")
    printParameters()
    
    
def initGame(initHp, initCoins, initDamage, initCount):
    global hp
    global coins
    global damage

    hp = initHp
    coins = initCoins
    damage = initDamage
    count = initCount

    print("Ты отправился в странствие навстречу приключениям и опасностям. Удачного путешествия!")
    printParameters()

def gameLoop():
    situation = r.randint(0, 4)

    if situation == 0:
        meetShop()
    elif situation == 1:
        meetMonster()
    elif situation == 3:
        Robert()
    else:
        input("Блуждаем...")

initGame(10, 15, 3)

while True:
    gameLoop()

    if hp <= 0:
        if input("Хочешь начать сначала (да/нет): ").lower() == "да":
            initGame(10, 15, 3)
        else:
            break