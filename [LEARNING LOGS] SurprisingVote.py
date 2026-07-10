"""docstring"""
def main():
    """asdasd"""
    score = float(input())
    max_score = float(input())
    one_score=score-(2*max_score)
    if one_score<0:
        one_score=0

    if max_score-one_score>2:
        print("Surprising")
    else:
        print("Not surprising")
main()
