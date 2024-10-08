import re
import time
import subprocess

# verificar a presença de loops
def check_for_loops(line):
    return bool(re.search(r"\bfor\b|\bwhile\b", line))

# verificar recursão
def check_for_recursion(line, function_name):
    return bool(function_name and re.search(r"\b" + re.escape(function_name) + r"\b", line))

# obter o nome da função (se houver)
def get_function_name(line, file_type):
    if file_type == 'c':
        match = re.match(r"\w+\s+(\w+)\s*\(.*\)\s*{", line)  # C
    elif file_type == 'py':
        match = re.match(r"def\s+(\w+)\s*\(", line)  # Python
    elif file_type == 'java':
        match = re.match(r"\w+\s+(\w+)\s*\(.*\)\s*{", line)  # Java
    else:
        return None
    
    if match:
        return match.group(1)
    return None

# verificar decisões locais 
def check_for_greedy(lines):
    greedy_patterns = [r"max\s*\(", r"min\s*\(", r"if\s*\(.*>", r"if\s*\(.*<"]
    for line in lines:
        for pattern in greedy_patterns:
            if re.search(pattern, line):
                return True
    return False

# verificar loops 
def check_for_nested_loops(lines):
    loop_depth = 0
    max_depth = 0
    for line in lines:
        line = line.strip()
        if check_for_loops(line):
            loop_depth += 1
            max_depth = max(max_depth, loop_depth)
        if "}" in line or re.match(r"^\s*end", line):  # C, Java ou Python com indentação
            loop_depth -= 1
    return max_depth

# medir o tempo de execução do código
def measure_execution_time(file_path):
    start_time = time.time()
    try:
       
        result = subprocess.run(["python3", file_path], capture_output=True, text=True, check=True)
        output = result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o código: {e}")
        output = e.output
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time, output

# analisar o código
def analyze_code(file_path, file_type):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Erro ao abrir o arquivo.")
        return
    
    loop_count = 0
    recursion_count = 0
    function_name = None
    is_greedy = check_for_greedy(lines)
    nested_loop_depth = check_for_nested_loops(lines)
    
    for line in lines:
        line = line.strip()

        # verificar se é a definição de uma função
        new_function_name = get_function_name(line, file_type)
        if new_function_name:
            function_name = new_function_name

        # verificar loops
        if check_for_loops(line):
            loop_count += 1

        # verificar recursão
        if check_for_recursion(line, function_name):
            recursion_count += 1

   
    print("\nAnálise Assintótica:\n")

    # melhor caso
    if loop_count == 0 and recursion_count == 0:
        print("- Melhor caso: Sem loops ou recursão encontrados. Complexidade O(1).")
    else:
        print("- Melhor caso: Pode variar dependendo da entrada, mas presença de loops e/ou recursões.")

    # pior caso
    if loop_count > 0:
        print(f"- Pior caso: O codigo contem {loop_count} loop(s) de profundidade máxima {nested_loop_depth}. Complexidade O(n^{nested_loop_depth}).")
    if recursion_count > 0:
        print(f"- Pior caso: O código contem {recursion_count} recursão(ões). Complexidade depende da função recursiva (O(T(n))).")
    if is_greedy:
        print("- Algoritmo potencialmente guloso: Baseado em decisões locais detectadas (ex., uso de max, min, etc.).")
    else:
        print("- Nenhum algoritmo guloso detectado.")

    
    if loop_count == 0 and recursion_count == 0:
        print("\nA análise resultou em um melhor caso de complexidade O(1).")
    elif loop_count > 0 and recursion_count == 0:
        print("\nA análise resultou em um pior caso, onde a complexidade está relacionada aos loops.")
    elif recursion_count > 0:
        print("\nA análise resultou em um pior caso, onde a complexidade depende da função recursiva.")
    
    # medir tempo de execução
    exec_time, output = measure_execution_time(file_path)
    print(f"\nTempo de execução estimado: {exec_time:.5f} segundos")
    print(f"Saída do código:\n{output}")


if __name__ == "__main__":
    while True:
        print("\nBem vindo, escolha o tipo de arquivo para analisar:\n")
        print("1. Arquivo .c")
        print("2. Arquivo .py")
        print("3. Arquivo .java")
        print("4. Sair")
        
        choice = input("\nDigite o número da sua escolha: ")

        if choice == '1':
            file_path = input("Digite o caminho do arquivo .c: ")
            analyze_code(file_path, 'c')
        elif choice == '2':
            file_path = input("Digite o caminho do arquivo .py: ")
            analyze_code(file_path, 'py')
        elif choice == '3':
            file_path = input("Digite o caminho do arquivo .java: ")
            analyze_code(file_path, 'java')
        elif choice == '4':
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Tente novamente.")
