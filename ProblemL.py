num_candidates, num_ballots = map(int, input().split())

candidates = [input()[2:] for _ in range(num_candidates)]
ballots = [list(map(int, input().split())) for _ in range(num_ballots)]


def validate_ballot(ballot):
    # check for duplicates
    if len(set(ballot)) != len(ballot):
        return False
    # check for valid votes
    for pick in ballot:
        if pick > num_candidates:
            return False
    # all good :)
    return True


ballots = list(filter(validate_ballot, ballots))
loser_indexes = []


def eliminate(candidate, votes):
    loser_indexes.append(candidates.index(candidate))
    print(f'{candidate} with {votes} votes is eliminated.')
    return candidates.index(candidate)


def declare_winner(winner):
    print(f'The winner of the election is {winner}.')
    exit()


def count_first_preference():
    # First, all the first-preference votes (on valid ballots) are counted.
    votes = {candidate: 0 for i, candidate in enumerate(
        candidates) if i not in loser_indexes}
    for ballot in ballots:
        if len(ballot):
            pick = candidates[ballot[0] - 1]
            if pick in votes:
                votes[pick] += 1
            else:
                votes[pick] = 1

    if len(ballots) == 1:
        declare_winner(list(ballots)[0])

    # After this count, if the number of votes for any candidate is more than half of the number of valid ballots, that candidate is declared the winner.
    for candidate in votes:
        if votes[candidate] > len(ballots) / 2:
            declare_winner(candidate)

    # Otherwise, the candidate(s) with the fewest number of votes is (are) eliminated.
    min_votes = min(votes, key=votes.get)
    losers = filter(lambda x: votes[x] == votes[min_votes], votes)
    [eliminate(loser, votes[loser]) for loser in losers]

    # Ballots that contain a vote for an eliminated candidate are modified by deleting that candidate, thereby “promoting” any lower-preference non-eliminated candidates. For example, if a ballot is “1 5 3” and candidate 5 is eliminated, the ballot becomes “1 3”.
    for i in loser_indexes:
        for ballot in ballots:
            while i + 1 in ballot:
                ballot.remove(i + 1)

    if list(filter(lambda x: len(x), ballots)):
        count_first_preference()
    else:
        print('The election was indecisive.')
        exit()


count_first_preference()
