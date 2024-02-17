from collections import Counter, defaultdict
import itertools
import math
import sys
import yaml

from retro.game_spec import GameSpec

def build_lineup_datas(years):
    alpha_games = defaultdict(list)
    alpha_by_year = {}

    most_inits = Counter()
    best_inits = {}

    for game in GameSpec.for_years(years):
        if game.date.year not in alpha_by_year:
            print(game.date.year)
            alpha_by_year[game.date.year] = len(alpha_games)

        for lineup in [game.away_lineup, game.home_lineup]:
            initials = [slot.player[4] + slot.player[0] for slot in lineup]
            initials += ['*' + slot.player[0] for slot in lineup]
            initials += [slot.player[4] + '*' for slot in lineup]
            inits = Counter(initials)

            for ii in inits:
                if inits[ii] >= most_inits[ii]:
                    most_inits[ii] = inits[ii]
                    best_inits[ii] = (game, lineup)

            alpha = tuple(
                (s.order, ix) for (ix, s) in enumerate(sorted(lineup, key=lambda s: s.player))
            )
            alpha = tuple(ix+1 for (order, ix) in sorted(alpha))
            alpha_games[alpha] += [(game, lineup)]

    return (most_inits, best_inits, alpha_games, alpha_by_year)

def print_best_initials(most_inits, best_inits):
    best_first = max((most_inits[ii] for ii in most_inits if ii[1] == '*'))
    best_last = max((most_inits[ii] for ii in most_inits if ii[0] == '*'))
    best_pair = max((most_inits[ii] for ii in most_inits if '*' not in ii))

    inits_to_print = [ii for ii in most_inits if ii[1] == '*' and most_inits[ii] == best_first]
    inits_to_print += [ii for ii in most_inits if ii[0] == '*' and most_inits[ii] == best_last]
    inits_to_print += [ii for ii in most_inits if '*' not in ii and most_inits[ii] == best_pair]

    out = []
    for ii in inits_to_print:
        #print(ii, most_inits[ii])
        (g, lu) = best_inits[ii]
        #print(g.date.date(), g.home_team, g.away_team, g.id)
        #print('; '.join(s.name for s in lu))
        #print('')
        out +=[{
            'initial': ii,
            'count': most_inits[ii],
            'date': g.date.date(),
            'id': g.id,
            'away': g.away_team,
            'home': g.home_team,
            'lineup': '; '.join(s.name for s in lu),
        }]
    yaml.dump(out, sys.stdout)

def print_grid(most_inits):
    print('   abcdefghijklmnopqrstuvwxyz *')
    for a in 'abcdefghijklmnopqrstuvwxyz*':
        print(a, ' ', end='')
        for b in 'abcdefghijklmnopqrstuvwxyz*':
            print(most_inits[a+b] or '.', end='')
            if b == 'z':
                print(' ', end ='')
        if a == 'z':
            print('')
        print('')

def print_most_sorted(alpha_games):
    def asc(l):
        return sum(x < y for (x,y) in itertools.combinations(l, 2))

    for k in sorted(alpha_games, key=lambda l: (-asc(l), l), reverse=False)[:10]:
        alph = alpha_games[k]
        print(k, f'{asc(k)}/36 {len(alph)} games')
        for (g, lu) in list(reversed(alph))[:5]:
            print(g.date.date(), g.home_team, g.away_team, '; '.join(s.name for s in lu))
        print('')

def print_permutations_by_year(alpha_games, alpha_by_year):
    for year in alpha_by_year:
        print(year, alpha_by_year[year], f'{(alpha_by_year[year] / math.factorial(9)):3f}')
    print(len(alpha_games), math.factorial(9), len(alpha_games) / math.factorial(9))


def main():
    yrs = list(range(1901, 2024))
    (most_inits, best_inits, alpha_games, alpha_by_year) = build_lineup_datas(yrs)

    print_best_initials(most_inits, best_inits)
    print('------')
    print_grid(most_inits)
    print('------')
    print_most_sorted(alpha_games)
    print('------')
    print_permutations_by_year(alpha_games, alpha_by_year)

main()
