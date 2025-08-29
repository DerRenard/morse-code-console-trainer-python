import assets.codes as code
import math
def quiz(lang, symbols):
  correct = 0
  incorrect = 0
  fullRange = 0
  tempDict = {}
  tempMistakes = []

  match (lang):
    case "en":
      match(symbols):
        case "nums":
          tempDict = code.morseEngCode | code.morseNumbers
          fullRange = len(tempDict)

          print("Выбрана латиница с числами\n")
          
          for key, value in tempDict.items():
            print(f"Для буквы {key} введите код: ")
            morse = input()
          
            if morse == value:
              print("correct \n")
              correct += 1
            else: 
              tempMistakes.append(key)
              print("incorrect \n")
              incorrect += 1
        
        case "sumb":
          tempDict = code.morseEngCode | code.morseSymbols
          fullRange = len(tempDict)
          
          print("Выбрана латиница с символами\n")
          
          for key, value in tempDict.items():
            print(f"Для буквы {key} введите код: ")
            morse = input()
          
            if morse == value:
              print("correct \n")
              correct += 1
            else: 
              tempMistakes.append(key)
              print("incorrect \n")
              incorrect += 1
        
        case "nums_sumb":
          tempDict = code.morseEngCode | code.morseNumbers | code.morseSymbols
          fullRange = len(tempDict)

          print("Выбрана латиница с числами и символами\n")
          
          for key, value in tempDict.items():
            print(f"Для буквы {key} введите код: ")
            morse = input()
          
            if morse == value:
              print("correct \n")
              correct += 1
            else: 
              tempMistakes.append(key)
              print("incorrect \n")
              incorrect += 1
        
        case _:
          tempDict = code.morseEngCode
          fullRange = len(tempDict)

          print("Выбрана латиница без чисел и символов\n")
          
          for key, value in tempDict.items():
            
            print(f"Для буквы {key} введите код: ")
            morse = input()

            if morse == value:
              print("correct \n")
              correct += 1
            else: 
              tempMistakes.append(key)
              print("incorrect \n")
              incorrect += 1

    case "ru":
      match(symbols):
        case "nums":
          tempDict = code.morseRusCode | code.morseNumbers
          fullRange = len(tempDict)

          print("Выбран русский с числами\n")
          
          for key, value in tempDict.items():
            print(f"Для буквы {key} введите код: ")
            morse = input()
          
            if morse == value:
              print("correct \n")
              correct += 1
            else: 
              tempMistakes.append(key)
              print("incorrect \n")
              incorrect += 1
        
        case "sumb":
          tempDict = code.morseRusCode | code.morseSymbols
          fullRange = len(tempDict)
          
          print("Выбран русский с символами\n")
          
          for key, value in tempDict.items():
            print(f"Для буквы {key} введите код: ")
            morse = input()
          
            if morse == value:
              print("correct \n")
              correct += 1
            else: 
              tempMistakes.append(key)
              print("incorrect \n")
              incorrect += 1
        
        case "nums_sumb":
          tempDict = code.morseRusCode | code.morseNumbers | code.morseSymbols
          fullRange = len(tempDict)

          print("Выбран русский с числами и символами\n")
          
          for key, value in tempDict.items():
            print(f"Для буквы {key} введите код: ")
            morse = input()
          
            if morse == value:
              print("correct \n")
              correct += 1
            else: 
              tempMistakes.append(key)
              print("incorrect \n")
              incorrect += 1
        
        case _:
          tempDict = code.morseRusCode
          fullRange = len(tempDict)

          print("Выбран русский без чисел и символов\n")
          
          for key, value in tempDict.items():
            print(f"Для буквы {key} введите код: ")
            morse = input()
            
            if morse == value:
              print("correct \n")
              correct += 1
            else: 
              tempMistakes.append(key)
              print("incorrect \n")
              incorrect += 1

    case _:
      match(symbols):
        case "nums":
          tempDict = code.morseNumbers
          fullRange = len(tempDict)

          print("Числа\n")
          
          for key, value in tempDict.items():
            print(f"Для буквы {key} введите код: ")
            morse = input()
          
            if morse == value:
              print("correct \n")
              correct += 1
            else: 
              tempMistakes.append(key)
              print("incorrect \n")
              incorrect += 1
        
        case "sumb":
          tempDict = code.morseSymbols
          fullRange = len(tempDict)
          
          print("Символы\n")
          
          for key, value in tempDict.items():
            print(f"Для буквы {key} введите код: ")
            morse = input()
          
            if morse == value:
              print("correct \n")
              correct += 1
            else: 
              tempMistakes.append(key)
              print("incorrect \n")
              incorrect += 1
        
        case "nums_sumb":
          tempDict = code.morseNumbers | code.morseSymbols
          fullRange = len(tempDict)

          print("Числа и символы\n")
          
          for key, value in tempDict.items():
            print(f"Для буквы {key} введите код: ")
            morse = input()
          
            if morse == value:
              print("correct \n")
              correct += 1
            else: 
              tempMistakes.append(key)
              print("incorrect \n")
              incorrect += 1
        
        case _:
          tempDict = code.morseNumbers
          fullRange = len(tempDict)

          print("Числа\n")
          
          for key, value in tempDict.items():
            print(f"Для буквы {key} введите код: ")
            morse = input()
          
            if morse == value:
              print("correct \n")
              correct += 1
            else: 
              tempMistakes.append(key)
              print("incorrect \n")
              incorrect += 1
  
  
  return {"correct": correct, "incorrect": incorrect, "range": fullRange, "mistakes": tempMistakes}