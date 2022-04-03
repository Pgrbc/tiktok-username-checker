import os, requests
from rich import print


def menu():
    os.system('cls && title username checker made by kaos [https://dsc.gg/kaos]')
    print("""
[#69C9D0]████████╗██╗██╗  ██╗[#EE1D52]████████╗ ██████╗ ██╗  ██╗
[#69C9D0]╚══██╔══╝██║██║ ██╔╝[#EE1D52]╚══██╔══╝██╔═══██╗██║ ██╔╝
[#69C9D0]   ██║   ██║█████╔╝ [#EE1D52]   ██║   ██║   ██║█████╔╝     - made by kaos#1951
[#69C9D0]   ██║   ██║██╔═██╗ [#EE1D52]   ██║   ██║   ██║██╔═██╗ 
[#69C9D0]   ██║   ██║██║  ██╗[#EE1D52]   ██║   ╚██████╔╝██║  ██╗
[#69C9D0]   ╚═╝   ╚═╝╚═╝  ╚═╝[#EE1D52]   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
""")

def write_file(arg: str) -> None:
    with open('hits.txt', 'a', encoding='UTF-8') as f:
        f.write(f'{arg}\n')

def check(username):
    check = requests.post(f'https://www.tiktok.com/@{username}')
    if check.status_code == 200:
        print(f'[red][-]https://www.tiktok.com/@{username}[/red]')
    else:
        print(f'[green][+]https://www.tiktok.com/@{username}[/green]')
        write_file(username)

menu()
try:
    with open('usernames.txt', 'r') as names:
        for name in names:
            check(name)
except FileNotFoundError:
    print("Please make a file called 'usernames.txt' and place the usernames you want to check in there")
    input()