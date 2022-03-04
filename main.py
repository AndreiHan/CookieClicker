import multiprocessing
import keyboard
import pyautogui

pyautogui.FAILSAFE = True


def click_main(clicks):
    for x in range(clicks):
        pyautogui.tripleClick(271, 503)
        pyautogui.tripleClick(272, 505)
        pyautogui.tripleClick(273, 507)
        pyautogui.tripleClick(274, 508)
        if keyboard.is_pressed("q"):
            print("You pressed q")
            break


def click_update0(clicks):
    for x in range(clicks):
        pyautogui.doubleClick(1832, 416)
        if keyboard.is_pressed("q"):
            print("You pressed q")
            break


def click_update1(clicks):
    for x in range(clicks):
        pyautogui.tripleClick(1830, 498)

        if keyboard.is_pressed("q"):
            print("You pressed q")
            break


def click_update2(clicks):
    for x in range(clicks):
        pyautogui.doubleClick(1832, 580)
        if keyboard.is_pressed("q"):
            print("You pressed q")
            break


def click_update3(clicks):
    for x in range(clicks):
        pyautogui.doubleClick(1832, 662)
        if keyboard.is_pressed("q"):
            print("You pressed q")
            break


def click_update4(clicks):
    for x in range(clicks):
        pyautogui.doubleClick(1832, 744)
        if keyboard.is_pressed("q"):
            print("You pressed q")
            break


def click_session(times):
    while True:
        if keyboard.is_pressed("s"):
            jobs = []
            for i in range(0, times):
                thread1 = multiprocessing.Process(target=click_main(10))
                thread2 = multiprocessing.Process(target=click_update4(1))
                thread3 = multiprocessing.Process(target=click_update3(1))
                thread4 = multiprocessing.Process(target=click_update2(1))
                thread5 = multiprocessing.Process(target=click_update1(1))
                thread6 = multiprocessing.Process(target=click_update0(1))

                jobs.append(thread1)
                jobs.append(thread2)
                jobs.append(thread3)
                jobs.append(thread4)
                jobs.append(thread5)
                jobs.append(thread6)

            for j in jobs:
                if keyboard.is_pressed("q"):
                    print("You pressed q")
                    break
                else:
                    j.start()

            for j in jobs:
                j.join()
            break

        if keyboard.is_pressed("q"):
            print("You pressed q")
            break


def ask_yesno(question):
    """
    Helper to get yes / no answer from user.
    """
    yes = {'yes', 'y', 'Y', ''}

    no = {'no', 'n', 'N'}

    done = False
    print()
    print(question)
    while not done:
        choice = input().lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            print("Please respond by yes(y/Y) or no(n/Y)")


def menu():
    while True:

        try:
            time = int(input('Enter time (in minutes) : '))
            print("Open Cookie Clicker and press on 's'")
            print("Moving the cursor to the upper left corner is the failsafe")
        except ValueError:
            print('Wrong input. Please enter a number ...')
        else:
            try:
                click_session(time * 10)
            except pyautogui.FailSafeException:
                print()
                print("Script Stopped by the user")

            if not ask_yesno("Do you want to go again?"):
                break
    print("Bye")


if __name__ == '__main__':

    try:
        menu()

    except KeyboardInterrupt:
        print()
        print("Script stopped by the user")
