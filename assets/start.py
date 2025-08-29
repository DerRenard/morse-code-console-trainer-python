def startOptons():
  lang = ["en", "ru", "no"]
  sumb = ["nums", "sumb", "nums_sumb"]

  print("Язык морзянки:\n1. en\n2. ru\n")
  langChoose = str(input("Выбор языка: "))
  print("\nДобавочные символы:\n1. nums\n2. sumb\n3. nums_sumb\nDefault: none\n")
  sumbChoose = str(input("Выбор добавочных: "))

  match(langChoose):
    case "1":
      match(sumbChoose):
        case "1":
          return {"lang": lang[int(langChoose) - 1], "sumb": sumb[int(sumbChoose) - 1]}
        case "2":
          return {"lang": lang[int(langChoose) - 1], "sumb": sumb[int(sumbChoose) - 1]}
        case "3":
          return {"lang": lang[int(langChoose) - 1], "sumb": sumb[int(sumbChoose) - 1]}
        case _:
          return {"lang": lang[int(langChoose) - 1], "sumb": "none"}
    case "2":
      match(sumbChoose):
        case "1":
          return {"lang": lang[int(langChoose) - 1], "sumb": sumb[int(sumbChoose) - 1]}
        case "2":
          return {"lang": lang[int(langChoose) - 1], "sumb": sumb[int(sumbChoose) - 1]}
        case "3":
          return {"lang": lang[int(langChoose) - 1], "sumb": sumb[int(sumbChoose) - 1]}
        case _:
          return {"lang": lang[int(langChoose) - 1], "sumb": "none"}
    case _:
      match(sumbChoose):
        case "1":
          return {"lang": "none", "sumb": sumb[int(sumbChoose) - 1]}
        case "2":
          return {"lang": "none", "sumb": sumb[int(sumbChoose) - 1]}
        case _:
          return {"lang": "none", "sumb": sumb[int(sumbChoose)]}