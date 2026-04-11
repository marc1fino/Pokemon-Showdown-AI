import asyncio
from tabulate import tabulate
from poke_env import cross_evaluate
from agents.random_agent import create_random_bot
from agents.maxdamage_agent import create_max_damage_bot


async def main():
    play_format = int(input("Are you playing in local server (1) or ladder (2): "))
    player1 = create_max_damage_bot(play_format)
    player2 = create_random_bot(play_format)
    players = [player1, player2]

    if play_format == 1:
        battles = int(input("Choose a number of battles to be played: "))
        while True:
            results = int(
                input("Choose way to show results: \n 1. Table / 2. Print \n")
            )
            if results == 2:
                await player1.battle_against(player2, n_battles=battles)
                print(f"Completed {battles} battles")
                print(f"Player {player1.username} victories: {player1.n_won_battles}")
                print(f"Player {player2.username} victories: {player2.n_won_battles}")
                break
            elif results == 1:
                cross_evaluation = await cross_evaluate(players, n_challenges=battles)
                table = [["-"] + [p.username for p in players]]
                for p_1, row in cross_evaluation.items():
                    table.append([p_1] + [cross_evaluation[p_1][p_2] for p_2 in row])
                print(f"Completed {battles} battles")
                print(tabulate(table))
                break
            else:
                print("Choose a correct answer")

    elif play_format == 2:
        battles = int(input("Choose a number of battles to be played: "))
        while True:
            player = int(
                input(
                    f"Choose what agent is going to play: \n 1. {player1.username} / 2. {player2.username} \n"
                )
            )
            if player == 1:
                await player1.ladder(battles)
                for battle in player1.battles.values():
                    print(battle.rating, battle.opponent_rating)
                break
            elif player == 2:
                await player2.ladder(battles)
                for battle in player2.battles.values():
                    print(battle.rating, battle.opponent_rating)
                break
            else:
                print("Choose a correct answer")
    else:
        print("Choose a correct answer")


if __name__ == "__main__":
    asyncio.run(main())
