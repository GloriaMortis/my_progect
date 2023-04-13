from funcs import plus_number, minum_number

choice_funcs = input("введите плюс или минус :")

numb_result = int

if choice_funcs == "плюс":
    numb_result = plus_number()
    print(numb_result)
elif choice_funcs == "минус":
    numb_result = minum_number()
    print(numb_result)
