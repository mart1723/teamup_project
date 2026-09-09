
import pygame
import game_filed
import soldier
import screen

state = {
    "window_open": True,
    "key_pressed": '',
    "touch_mine": False,
    "touch_flag": False,

}

def main():
    pygame.init()
    # create screen and objects
    charter = soldier.create_soldier()
    info = game_filed.first_creat(charter)
    flag_cord = info[0]
    mine_map = info[1]
    bush_map = info[2]
    screen.create_day_screen(charter, bush_map)
    screen.create_night_screen(charter, mine_map, bush_map)

    is_running = True
    direction = ["up", "down", "left", "right"]

    while is_running:
        event_handler(charter)

        if state["key_pressed"] in direction:
            game_filed.move_soldier(charter, state["key_pressed"])
        elif state["key_pressed"] == "enter":
            screen.draw_night_screen(charter, mine_map, bush_map)

        if soldier.touch_mine(charter, mine_map):
            state["touch_mine"] = True
            print("Mine")

        if soldier.touch_flag(charter, flag_cord):
            state["touch_flag"] = True
            print("Flag")

        if state["touch_flag"]:
            win()
        elif state["touch_mine"]:
            lose()
            is_running = False

        screen.draw_day_screen(charter, bush_map)




def event_handler(charter):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                state["key_pressed"] = "up"
            elif event.key == pygame.K_DOWN:
                state["key_pressed"] = "down"
            elif event.key == pygame.K_LEFT:
                state["key_pressed"] = "left"
            elif event.key == pygame.K_RIGHT:
                state["key_pressed"] = "right"
            elif event.key == pygame.K_RETURN:
                state["key_pressed"] = "enter"
        if event.type == pygame.KEYUP:
            state["key_pressed"] = None

def lose():

    pygame.quit()

def win():

    pygame.quit()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()