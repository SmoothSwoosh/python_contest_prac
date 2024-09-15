def norm_records(image):
    normalized_records = []
    for rectangle in image:
        x, y, w, h, character = rectangle
        if w * h == 0:
            continue
        if w < 0:
            x -= (w := -w)
        if h < 0:
            y -= (h := -h)
        normalized_records.append(list([x, y, w, h, character]))

    return normalized_records


def read_and_process_data():
    image = []
    #read image
    while rectangle := input().split():
        image.append(rectangle)

    #process image
    for i, rectangle in enumerate(image):
        image[i] = list(map(int, rectangle[:-1])) + list(rectangle[-1])

    #get records of rectangles in normal form
    return norm_records(image)


def get_canvas_size(image):
    if not image:
        return (0, 0, 0, 0)
    
    left, up, right, down = float('inf'), float('inf'), \
                            float('-inf'), float('-inf')
    for rectangle in image:
        x, y, w, h, character = rectangle
        left = min(left, x)
        up = min(up, y)
        right = max(right, x + w - 1)
        down = max(down, y + h - 1)

    return (left, up, right, down)


def scale_to_canvas(canvas_size, image):
    left, up, right, down = canvas_size
    for i, rectangle in enumerate(image):
        x, y, w, h, character = rectangle
        x -= left
        y -= up
        image[i] = list([x, y, w, h, character])

    return image


def draw_image(image):
    if not image:
        return []
    
    canvas = [['.'] * width for i in range(height)]
    
    for rectangle in image:
        x, y, w, h, character = rectangle
        for i in range(h):
            for j in range(w):
                canvas[y + i][x + j] = character

    return canvas   


def print_canvas(canvas):
    for line in canvas:
        print(*line, sep='',end='\n')


image = read_and_process_data()
canvas_size = get_canvas_size(image)
image = scale_to_canvas(canvas_size, image)
left, up, right, down = canvas_size
width, height = right - left + 1, down - up + 1
canvas = draw_image(image)
print_canvas(canvas)

