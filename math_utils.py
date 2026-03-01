import matplotlib.pyplot as plt

def fibonacci(n):
    """
    生成前 n 个斐波那契数列。
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def visualize_fibonacci(n):
    """
    计算并可视化前 n 个斐波那契数。
    """
    sequence = fibonacci(n)
    
    # 设置图表风格
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 绘制柱状图
    indices = range(len(sequence))
    ax.bar(indices, sequence, color='skyblue', alpha=0.7, label='Fibonacci Value')
    
    # 绘制折线图
    ax.plot(indices, sequence, marker='o', color='darkblue', linewidth=2, label='Growth Trend')
    
    # 添加数值标签
    for i, v in enumerate(sequence):
        ax.text(i, v + (max(sequence) * 0.02), str(v), ha='center', va='bottom', fontsize=9)
    
    # 设置标题和标签
    ax.set_title(f'Visualization of First {n} Fibonacci Numbers', fontsize=14)
    ax.set_xlabel('Index', fontsize=12)
    ax.set_ylabel('Value', fontsize=12)
    ax.set_xticks(indices)
    ax.legend()
    
    # 保存图片并提示
    output_file = 'fibonacci_plot.png'
    plt.savefig(output_file)
    print(f"可视化图表已保存至: {output_file}")
    plt.close()

if __name__ == "__main__":
    n = 10
    print(f"Fibonacci sequence (first {n} numbers): {fibonacci(n)}")
    visualize_fibonacci(n)
