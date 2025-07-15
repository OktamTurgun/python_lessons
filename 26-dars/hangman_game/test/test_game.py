import pytest
from unittest.mock import patch
from hangman.game import clean_words, display_word, get_random_word, play_game

def test_clean_words_removes_invalid():
  raw = ["salom", "kitob", "_noto'g'ri", "2dunyo", "ona tili", "py thon"]
  cleaned = clean_words(raw)
  assert cleaned == ["SALOM", "KITOB"]

def test_display_word_partial():
  word = "KITOB"
  guessed = {'K', 'O'}
  result = display_word(word, guessed)
  assert result == "K _ _ O _"

def test_display_word_full():
  word = "DARAJA"
  guessed = set("DARAJ")
  result = display_word(word, guessed)
  assert result == "D A R A J A"

def test_get_random_word_is_in_list():
  word_list = ["SALOM", "DUNYO", "KITOB"]
  word = get_random_word(word_list)
  assert word in word_list

def test_play_game_win(monkeypatch, capsys):
  # So'z: "KITOB", harflar: K, I, T, O, B
  inputs = iter(['K', 'I', 'T', 'O', 'B'])
  with patch('hangman.game.words', ["KITOB"]), \
     patch('builtins.input', lambda _: next(inputs)):
    play_game(max_attempts=10)
  output = capsys.readouterr().out
  assert "🎉 Tabriklaymiz! Siz 'KITOB' so'zini" in output

def test_play_game_lose(monkeypatch, capsys):
  # So'z: "SALOM", noto'g'ri harflar: Q, W, E, R, T, Y, U, I, P, Z
  inputs = iter(['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'P', 'Z'])
  with patch('hangman.game.words', ["SALOM"]), \
     patch('builtins.input', lambda _: next(inputs)):
    play_game(max_attempts=10)
  output = capsys.readouterr().out
  assert "😞 Yutqazdingiz! So'z bu edi: 'SALOM'" in output

def test_play_game_invalid_input(monkeypatch, capsys):
  # So'z: "KITOB", noto'g'ri va to'g'ri harflar aralash
  inputs = iter(['1', 'K', '!', 'I', 'K', 'T', 'O', 'B'])
  with patch('hangman.game.words', ["KITOB"]), \
     patch('builtins.input', lambda _: next(inputs)):
    play_game(max_attempts=10)
  output = capsys.readouterr().out
  assert "Faqat 1 dona harf kiriting." in output
  assert "'K' harfini allaqachon kiritgansiz." in output
  assert "🎉 Tabriklaymiz! Siz 'KITOB' so'zini" in output

def test_play_game_no_valid_words(capsys):
  with patch('hangman.game.words', []):
    play_game(max_attempts=5)
  output = capsys.readouterr().out
  assert "So'zlar ro'yxatida yaroqli so'zlar topilmadi." in output