input.onButtonPressed(Button.A, function () {
    if (실행중 == 1) {
        if (발사중 == 0) {
            led.unplot(player_x, 4)
            player_x += -1
            if (player_x == -1) {
                player_x = 4
            }
            led.plotBrightness(player_x, 4, 150)
        }
    }
})
input.onButtonPressed(Button.AB, function () {
    if (실행중 == 1) {
        발사중 = 1
        bullet_y = 4
        bullet_x = player_x
        for (let index = 0; index < 5; index++) {
            led.plotBrightness(bullet_x, bullet_y, 255)
            basic.pause(50)
            led.unplot(bullet_x, bullet_y)
            bullet_y += -1
            led.plotBrightness(player_x, 4, 150)
        }
        발사중 = 0
    }
})
input.onButtonPressed(Button.B, function () {
    if (실행중 == 1) {
        if (발사중 == 0) {
            led.unplot(player_x, 4)
            player_x += 1
            if (player_x == 5) {
                player_x = 0
            }
            led.plotBrightness(player_x, 4, 150)
        }
    }
})
let enemy_발사 = 0
let 마지막_위치 = 0
let 점수 = 0
let en_bu_y = 0
let en_bu_x = 0
let enemy_이동 = 0
let bullet_x = 0
let bullet_y = 0
let 발사중 = 0
let player_x = 0
let 실행중 = 0
실행중 = 1
let enemy_x = 4
player_x = 2
발사중 = 0
led.plotBrightness(player_x, 4, 150)
loops.everyInterval(2000, function () {
    if (실행중 == 1) {
        enemy_이동 = 1
    }
})
basic.forever(function () {
    if (en_bu_x == player_x && en_bu_y == 4) {
        실행중 = 0
        basic.showString("DEAD!")
        basic.showString("SCORE IS" + ("" + 점수))
    }
    if (bullet_x == enemy_x && bullet_y == 0) {
        점수 += 1
    }
})
basic.forever(function () {
    if (실행중 == 1) {
        if (enemy_이동 == 1) {
            마지막_위치 = player_x
            led.unplot(enemy_x, 0)
            enemy_x = player_x
            led.plotBrightness(enemy_x, 0, 50)
            enemy_이동 = 0
        }
        if (enemy_발사 == 1) {
            en_bu_y = 0
            en_bu_x = enemy_x
            for (let index = 0; index < 5; index++) {
                led.plotBrightness(en_bu_x, en_bu_y, 200)
                basic.pause(200)
                led.unplot(en_bu_x, en_bu_y)
                en_bu_y += 1
                led.plotBrightness(enemy_x, 0, 50)
            }
            enemy_발사 = 0
        }
    }
})
loops.everyInterval(5000, function () {
    if (실행중 == 1) {
        enemy_발사 = 1
    }
})
