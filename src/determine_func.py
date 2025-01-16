TypeErrorMessage = "Incorrect offset. Offset must be <str>, <float>, <byte> or <int>."
ValueErrorMessage = "Invalid literal for int() with base 10: <{offset}>."
NotFoundMessage = "Offset not found."


def get_score(game_stamps, offset):
    '''
        Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
        Please pay attention to that for some offsets the game_stamps list may not contain scores.
    '''
    try:
        offset = int(offset)
    except (TypeError, ValueError) as exc:
        if isinstance(exc, ValueError):
            return ValueErrorMessage.format(offset=offset)
        return TypeErrorMessage
    for stamp in game_stamps:
        if int(offset) == stamp["offset"]:
            return stamp["score"]["home"], stamp["score"]["away"]
    return NotFoundMessage
