sts = pstats.Stats("hoge.prof")
sts.strip_dirs().sort_stats("cumtime").print_stats(30)
