import id3
import mlp
import pandas
from sklearn.metrics import confusion_matrix

def ConfusionMatrixID3(result_tree, test_iris):
    # target results
    target_results = (id3.get_results(result_tree, [], test_iris, False)[1])
    arranged_target_results = []
    for x in target_results:
        arranged_target_results.append(x)
    target_results = arranged_target_results

    # hasil yang didapat dari algo
    results = (id3.get_results(result_tree, [], test_iris, False)[0])

    # membuat confusion matrix dari sklearn
    return confusion_matrix(target_results, results, labels=['Virginica', 'Versicolor', 'Setosa'])

def ConfusionMatrixMLP(result_model, test_iris):
    attributes = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']
    result_labels = ['Virginica', 'Versicolor', 'Setosa']
    result_column_name = 'variety'
    target_results = mlp.get_results(result_model, attributes, result_labels, result_column_name, test_iris)[0]

    results = mlp.get_results(result_model, attributes, result_labels, result_column_name, test_iris)[1]

    # membuat confusion matrix dari sklearn
    return confusion_matrix(target_results, results, labels=['Virginica', 'Versicolor', 'Setosa'])

def ID3(df):
    # memisahkan data training dan testing dengan perbandingan 9:1
    separator_iris = round((9/10)*len(df.index))
    train_iris = df.iloc[:separator_iris, :].reset_index(drop = True)
    test_iris = df.iloc[separator_iris:, :].reset_index(drop = True)

    # pembelajaran dengan training data
    result_tree = id3.ID3(df, train_iris, test_iris, True)

    # menghitung kinerja
    result_accuracy = id3.count_accuracy(result_tree, [], test_iris, True)

    # menampilkan tree hasil
    id3.print_tree(result_tree, 0)
    print('Akurasi :')
    print(result_accuracy)
    print('Confussion Matrix untuk Virginica, Versicolor, Setosa :')
    print(ConfusionMatrixID3(result_tree, test_iris))

def MLP(df, num_perceptrons_in_layer, max_iteration, error_threshold, learning_rate, batch_size):
    # memisahkan data training dan testing dengan perbandingan 9:1
    separator_iris = round((9/10)*len(df.index))
    train_iris = df.iloc[:separator_iris, :].reset_index(drop = True)
    test_iris = df.iloc[separator_iris:, :].reset_index(drop = True)

    # pembelajaran dengan training data
    result_model = mlp.MLP(train_iris, num_perceptrons_in_layer, max_iteration, error_threshold, learning_rate, batch_size)

    # menghitung kinerja
    result_accuracy = mlp.count_accuracy(result_model, test_iris)

    # menampilkan tree hasil
    result_model.print_model()
    print('Akurasi :')
    print(result_accuracy)
    print('Confussion Matrix untuk Virginica, Versicolor, Setosa :')
    print(ConfusionMatrixMLP(result_model, test_iris))
