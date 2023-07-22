import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

def parse_input(input_data):
    site_points, vertex_points, line_segments = [], [], []

    line_counter, vertex_counter = 0,0

    for line in input_data:
        if line.startswith('s'):
            _, x, y = line.split()
            site_points.append([float(x), float(y)])
        elif line.startswith('l'):
            _, a, b, c = line.split()
            line_segments.append([[float(a), float(b), float(c)]])
            line_counter += 1
        elif line.startswith('v'):
            _, x, y = line.split()
            vertex_points.append([float(x), float(y)])
            vertex_counter += 1
        elif line.startswith('e'):
            _, line_idx, left_idx, right_idx = line.split()
            line_segments[int(line_idx)].append([int(left_idx), int(right_idx)])

    return site_points, vertex_points, line_segments

def plot_voronoi(site_points, vertex_points, line_segments):
    lines = []
    line_labels = []
    for i, segment in enumerate(line_segments):
        left, right = segment[1]
        if left == -1:
            x1, y1 = vertex_points[int(right)]
            x = -1e6
            if segment[0][1] != 0:
                y = (segment[0][2] - segment[0][0] * x) / segment[0][1]
            else:
                y = y1
            lines.append([[x, y], [x1,y1]])
        elif right == -1:
            x1, y1 = vertex_points[int(left)]
            x = 1e6
            if segment[0][1] != 0:
                y = (segment[0][2] - segment[0][0] * x) / segment[0][1]
            else:
                y = y1
            lines.append([[x1,y1], [x, y]])
        else:
            lines.append([vertex_points[int(left)], vertex_points[int(right)]])
            

    lines_collection = LineCollection(lines)

    fig, ax = plt.subplots(figsize=(16, 9))
    ax.set_xlim(-1, 2)
    ax.set_ylim(-1, 2)
    ax.add_collection(lines_collection)

    for i, point in enumerate(site_points):
        ax.plot(point[0], point[1], 'ro')
        #ax.text(point[0] + 0.5, point[1] + 0.5, f'Site {i}', color='red')

    for i, point in enumerate(vertex_points):
        ax.plot(point[0], point[1], 'go')
        #ax.text(point[0] + 0.5, point[1] + 0.5, f'Vertex {i}', color='green')

    plt.show()


if __name__ == '__main__':
    
    file_path = './c_code_output.txt' 

    with open(file_path, 'r') as file:
        input_data = file.readlines()

    site_points, vertex_points, line_segments = parse_input(input_data)
    plot_voronoi(site_points, vertex_points, line_segments)
