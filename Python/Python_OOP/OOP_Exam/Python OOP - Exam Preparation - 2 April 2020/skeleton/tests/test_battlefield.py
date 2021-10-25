from unittest import TestCase, main

from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.battle_field import BattleField


class TestBattlefield(TestCase):
    def setUp(self):
        self.attacker = Beginner("Bushido")
        self.enemy = Beginner("Onyx")
        self.attacker.card_repository.cards = [MagicCard("Some magic card"), TrapCard("Some trap card"),
                                               MagicCard("Some magic card"), TrapCard("Some trap card"),
                                               MagicCard("Some magic card"), TrapCard("Some trap card")]
        self.enemy.card_repository.cards = [MagicCard("Some magic card"), TrapCard("Some trap card"),
                                            MagicCard("Some magic card"), TrapCard("Some trap card")]

    def test_init(self):
        self.assertEqual("Bushido", self.attacker.username)
        self.assertEqual("Onyx", self.enemy.username)
        self.assertEqual(50, self.attacker.health)
        self.assertEqual(50, self.enemy.health)

    def test_fight_attacker_or_enemy_is_dead_zero_raises(self):
        self.assertEqual(50, self.attacker.health)
        self.assertEqual(50, self.enemy.health)
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            BattleField.fight(self.attacker, self.enemy)
        self.assertEqual("Player is dead!", str(ex.exception))

    def test_fight_attacker_is_beginner(self):
        self.assertEqual(50, self.attacker.health)
        self.assertEqual(50, self.enemy.health)
        self.enemy.health += 110
        BattleField.fight(self.attacker, self.enemy)
        self.assertEqual(345, self.attacker.health)
        self.assertEqual(0, self.enemy.health)

    def test_fight_increase_health(self):
        attacker = Advanced("Bushido")
        enemy = Advanced("Onyx")
        card = TrapCard("Exodia")
        attacker.card_repository.cards.append(card)
        enemy.card_repository.cards.append(card)
        BattleField.fight(attacker, enemy)
        self.assertEqual(135, attacker.health)
        self.assertEqual(135, enemy.health)
        self.assertFalse(attacker.is_dead)
        self.assertFalse(enemy.is_dead)


if __name__ == '__main__':
    main()
