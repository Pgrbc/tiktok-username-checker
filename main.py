import os
import time
import asyncio
from os import system
from typing import List
from rich import print
import aiohttp




def write_file(arg: str) -> None:
    with open('hits.txt', 'a', encoding='UTF-8') as f:
        f.write(f'{arg}\n')


class Checker:
    def __init__(self, usernames: List[str]):
        self.to_check = usernames

    async def _check(self, session: aiohttp.ClientSession, username: str) -> None:
        async with session.head(f'https://www.tiktok.com/@{username}') as response:
            if response.status == 200:
                print(f'[red][-] https://www.tiktok.com/@{username}')
            elif response.status == 404:
                print(f'[green][+] https://www.tiktok.com/@{username}')
                write_file(username)
            elif response.status == 403:
                print("[yellow][!]Being ratelimited, waiting 10 seconds and trying again")
                time.sleep(10)

    async def start(self):
        print('Loading, please hang on')
        async with aiohttp.ClientSession() as sess:
            return await asyncio.gather(*[self._check(sess, u) for u in self.to_check])


if __name__ == '__main__':
    system('cls && title username checker made by kaos [https://dsc.gg/kaos]')
    print("""
[#69C9D0]████████╗██╗██╗  ██╗[#EE1D52]████████╗ ██████╗ ██╗  ██╗
[#69C9D0]╚══██╔══╝██║██║ ██╔╝[#EE1D52]╚══██╔══╝██╔═══██╗██║ ██╔╝
[#69C9D0]   ██║   ██║█████╔╝ [#EE1D52]   ██║   ██║   ██║█████╔╝     - made by kaos#1951
[#69C9D0]   ██║   ██║██╔═██╗ [#EE1D52]   ██║   ██║   ██║██╔═██╗ 
[#69C9D0]   ██║   ██║██║  ██╗[#EE1D52]   ██║   ╚██████╔╝██║  ██╗
[#69C9D0]   ╚═╝   ╚═╝╚═╝  ╚═╝[#EE1D52]   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
""")
    try:
        with open('usernames.txt', encoding='UTF-8') as f:
            username_list = [line.strip() for line in f]
    except FileNotFoundError:
        print("Please make a file called 'usernames.txt' and put the usernames you wanna check in there")
        input()

    checker = Checker(username_list)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(checker.start())
    print("Press enter to exit")
    input()
