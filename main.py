def on_button_pressed_a():
    global player_x
    if 실행중 == 1:
        if 발사중 == 0:
            led.unplot(player_x, 4)
            player_x += -1
            if player_x == -1:
                player_x = 4
            led.plot_brightness(player_x, 4, 150)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global 발사중, bullet_y, bullet_x
    if 실행중 == 1:
        발사중 = 1
        bullet_y = 4
        bullet_x = player_x
        for index in range(5):
            led.plot_brightness(bullet_x, bullet_y, 255)
            basic.pause(50)
            led.unplot(bullet_x, bullet_y)
            bullet_y += -1
            led.plot_brightness(player_x, 4, 150)
        발사중 = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global player_x
    if 실행중 == 1:
        if 발사중 == 0:
            led.unplot(player_x, 4)
            player_x += 1
            if player_x == 5:
                player_x = 0
            led.plot_brightness(player_x, 4, 150)
input.on_button_pressed(Button.B, on_button_pressed_b)

점수 = 0
en_bu_x = 0
en_bu_y = 0
enemy_발사 = 0
마지막_위치 = 0
bullet_x = 0
bullet_y = 0
발사중 = 0
player_x = 0
실행중 = 0
실행중 = 1
enemy_x = 4
enemy_이동 = 0
player_x = 2
발사중 = 0
led.plot_brightness(player_x, 4, 150)

def on_every_interval():
    global enemy_이동
    if 실행중 == 1:
        enemy_이동 = 1
loops.every_interval(2000, on_every_interval)

def on_forever():
    global 마지막_위치, enemy_x, enemy_이동, en_bu_y, en_bu_x, enemy_발사
    if 실행중 == 1:
        if enemy_이동 == 1:
            마지막_위치 = player_x
            led.unplot(enemy_x, 0)
            enemy_x = player_x
            led.plot_brightness(enemy_x, 0, 50)
            enemy_이동 = 0
        if enemy_발사 == 1:
            en_bu_y = 0
            en_bu_x = enemy_x
            for index2 in range(5):
                led.plot_brightness(en_bu_x, en_bu_y, 200)
                basic.pause(200)
                led.unplot(en_bu_x, en_bu_y)
                en_bu_y += 1
                led.plot_brightness(enemy_x, 0, 50)
            enemy_발사 = 0
basic.forever(on_forever)

def on_forever2():
    global 실행중, 점수
    if en_bu_x == player_x and en_bu_y == 4:
        실행중 = 0
        basic.show_string("DEAD!")
        basic.show_string("SCORE IS" + str(점수))
    if bullet_x == enemy_x and bullet_y == 0:
        점수 += 1
basic.forever(on_forever2)

def on_every_interval2():
    global enemy_발사
    if 실행중 == 1:
        enemy_발사 = 1
loops.every_interval(5000, on_every_interval2)
