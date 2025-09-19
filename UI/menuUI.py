while(True):
    print('--- MENU ---')
    try:
        option = int(input('1 - Entrar em uma instituição já registrada.\n2 - Registrar nova instituição\n0 - Sair\n'))
    except:
        print('Insira um valor válido.')
        continue

    match option:
        case 0:
            print('escolheu 0')
        case 1:
            print('escolheu 1')
        case 2:
            print('escolheu 2')
        case _:
            print('Insira um valor válido.')
            continue
