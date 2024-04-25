import my_functions as mf
import my_bfs
import my_dfs
import my_a_star
import my_metrics
import sys

def run_algorithm(algorithm_name, metric_or_order, board):
    if algorithm_name == 'bfs':
        results = my_bfs.bfs(board, metric_or_order)
        return results
    elif algorithm_name == 'dfs':
        results = my_dfs.dfs(board, metric_or_order)
        return results
    elif algorithm_name == 'astr':
        if metric_or_order == 'manh':
            results = my_a_star.a_star(board, my_metrics.manhattan_metric)
            return results
        elif metric_or_order == 'hamm':
            results = my_a_star.a_star(board, my_metrics.haming_metric)
            return results
        else:
            raise Exception('Wrong metric name')
    else:
        raise Exception('Wrong algorithm_name')

def main():
    # check if there is correct amount of arguments
    if len(sys.argv) != 6:
        print("usage: <program_name> <algorithm_name> <metric_or_order> <input_file> <output_file> <stats_file>")
        sys.exit(1)

    # arguments pars
    script_name, algorithm_name, metric_or_order, input_file, output_file, stats_file = sys.argv
    # loading board from file
    board = mf.import_board(input_file)
    # run algorithm
    result = run_algorithm(algorithm_name, metric_or_order, board)

    # saving path and len of path
    save_path = "/Users/arek/2.Repos4thSemester/sise2024/algorithms/path_files/{}".format(output_file)
    with open(save_path, 'w') as f:
        if result[0]:
            # len of path
            f.write(result[2])
            f.write('\n')
            # path
            f.write(result[1])
        else:
            f.write(result[2])

    # saving stats
    stats_path = "/Users/arek/2.Repos4thSemester/sise2024/algorithms/stats_files/{}".format(stats_file)
    with open(stats_path, 'w') as f:
        # len of path
        f.write(result[2])
        f.write('\n')
        # visited elements
        f.write(result[3])
        f.write('\n')
        # processed elements
        f.write(result[4])
        f.write('\n')
        # max depth
        f.write(result[5])
        f.write('\n')
        # time
        time = str(round(float(result[6]), 3))
        f.write(time)



if __name__ == '__main__':
    main()

