import my_functions as mf
import my_bfs as bfs
import my_dfs as dfs
import my_a_star as a_star
import my_metrics
import sys



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
    with open(output_file, 'w') as f:
        if result[0]:
            # len of path
            f.write(result[2])
            # path
            f.write(result[1])
        else:
            f.write(result[2])

    # saving stats
    with open(stats_file, 'w') as f:
        # len of path
        f.write(result[2])
        # visited elements
        f.write(result[3])
        # processed elements
        f.write(result[4])
        # max depth
        f.write(result[5])
        # time
        time = round(float(result[6]), 3)
        f.write(time)



if __name__ == '__main__':
    main()

def run_algorithm(algorithm_name, metric_or_order, board):
    if algorithm_name == 'bfs':
        return bfs(board, metric_or_order)
    elif algorithm_name == 'dfs':
        return dfs(board, metric_or_order)
    elif algorithm_name == 'astr':
        if metric_or_order == 'manh':
            return a_star(board, my_metrics.manhattan_metric)
        elif metric_or_order == 'hamm':
            return a_star(board, my_metrics.haming_metric)
        else:
            raise Exception('Wrong metric name')
    else:
        raise Exception('Wrong algorithm_name')