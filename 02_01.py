name = input("こんにちは、お名前を教えてください。")
age = int(input("何歳ですか？"))

if (age < 13): 
    print("あなたは若すぎます", name)
else:
    print("お気軽にご参加ください", name)