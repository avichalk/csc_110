#Author: Avichal Kaul
#Description: Takes two input ppm files and some user inputs, and
## chroma keys bits of the first image out to replace them with pixels
## from the second image. It ouputs this into a third ppm file that was
## specified by the user.
#Comments: This was a really fun class. I had some issues, but it was
## still really amazing. thank you, guys, but also please take our
## feedback into account.

def get_image_dimensions_string(file_name):
    '''
    Given the file name for a valid PPM file, this function will return the
    image dimensions as a string. For example, if the image stored in the
    file is 150 pixels wide and 100 pixels tall, this function should return
    the string '150 100'.
    file_name: A string. A PPM file name.
    '''
    image_file = open(file_name, 'r')
    image_file.readline()
    return image_file.readline().strip('\n')

def load_image_pixels(file_name):
    ''' Load the pixels from the image saved in the file named file_name.
    The pixels will be stored in a 3d list, and the 3d list will be returned.
    Each list in the outer-most list are the rows of pixels.
    Each list within each row represents and individual pixel.
    Each pixels is representd by a list of three ints, which are the RGB values of that pixel.
    '''
    pixels = []
    image_file = open(file_name, 'r')

    image_file.readline()
    image_file.readline()
    image_file.readline()

    width_height = get_image_dimensions_string(file_name)
    width_height = width_height.split(' ')
    width = int(width_height[0])
    height = int(width_height[1])

    for line in image_file:
        line = line.strip('\n ')
        rgb_row = line.split(' ')
        row = []
        for i in range(0, len(rgb_row), 3):
            pixel = [int(rgb_row[i]), int(rgb_row[i+1]), int(rgb_row[i+2])]
            row.append(pixel)
        pixels.append(row)

    return pixels

def main():
    '''
    Our main function handles all the user inputs, and
    makes calls to several other functions- including our
    starter code functions. It also validates
    all our inputs as they're being inputted. It prints
    our 'output value written' message, but doesn't
    return anything.
    '''
    channel = input('Enter color channel\n')
    if channel=='r' or channel=='g' or channel=='b':
        '' ## validating inputs
    else:
        print('Channel must be r, g, or b. Will exit.')
        return ## this is the only way i found to exit the program gracefully
    channel_difference = input('Enter color channel difference\n')
    if float(channel_difference)>=1.0 and float(channel_difference)<=10.0:
        ''
    else:
        print('Invalid channel difference. Will exit.')
        return

    gs_file = input('Enter greenscreen image file name\n')
    fi_file = input('Enter fill image file name\n')
    if get_image_dimensions_string(gs_file)==get_image_dimensions_string(fi_file):
        '' ## checking that the height and width of the images are the same
    else:
        print('Images not the same size. Will exit.')
        return
    out_file = input('Enter output file name\n')

    print('Output file written. Exiting.')

    gs_file_data=load_image_pixels(gs_file)
    fi_file_data=load_image_pixels(fi_file)

    output_file_data = greenscreen(channel, channel_difference, gs_file_data, fi_file_data)
    print_to_file(output_file_data, out_file)


def greenscreen(channel, channel_difference, gs_file_data, fi_file_data):
    '''
    This function takes the raw ppm image data from main and uses an
    algorithm to determine whether a pixel should be replaced or not
    by looping through a 3d list. It has no user inputs, but does return
    a list of image data to main.
    '''
    x, output_file_data = 69, [] ## this line brings the function line count to
    if channel=='r': ## exactly 30
        x=0 ## this changes the index in the list depending on the user inputted
    elif channel=='g': ## color channel
        x=1
    elif channel=='b':
        x=2
    i=0 ## start of our algorithm and massive loop
    while i<len(gs_file_data):
        k=0
        output_file_data_1=[] ## this is a different, temporary list that makes formatting easier
        while k<len(gs_file_data[i]): ## and gets reset each time the 'i' while loop loops
            y=0
            z=0
            while y<3:
                if gs_file_data[i][k][y]==0: ## this is for cases where the color value is 0
                    if gs_file_data[i][k][x]!=0: ## since that causes a div by 0 error
                        z+=1
                else:
                    if float(gs_file_data[i][k][x]/gs_file_data[i][k][y])>float(channel_difference):
                        z+=1 ## this is most of the algorithm- if the pixel brightness compared to the
                y+=1 ## other pixel values is more than the channel difference, it adds 1 to z.
            if z==2: ## if z=2, it means this is true for both pixels that aren't the color channel
                output_file_data_1.append(fi_file_data[i][k]) ## pixel, and it adds the other image's
                k+=1 ## pixel to our output data list.
            else:
                output_file_data_1.append(gs_file_data[i][k]) ## otherwise, it keeps out original image's
                k+=1 ## pixel.
        i+=1 ## this is just to deal with how our pixel values are fed to us by the starter code and how
        output_file_data.append(output_file_data_1) ## ppm files store pixel data.
    return output_file_data

def print_to_file(output_file_data, out_file):
    '''
    This function accepts a 3d list of pixel data from main
    along with a filename, and creates a file with said filename
    that it prints our image data to. It does not return or print
    any values.
    '''
    output_file=open(out_file, 'w')
    output_file.write('P3\n') ## this is for the ppm file format
    to_write=str(len(output_file_data[0]))+' '+str(len(output_file_data))+' \n'
    output_file.write(str(to_write)) ## the length and height of the image
    output_file.write('255\n') ## the max subpixel brightness of a pixel
    i=0
    while i<len(output_file_data):
        j=0
        string=''
        while j<len(output_file_data[i]):
            k=0
            while k<len(output_file_data[i][j]):
                string+=str(output_file_data[i][j][k])
                string+=' '
                k+=1
            j+=1 ## getting a string from our list that we can use to write
        string+='\n' ## to the file using the correct format
        output_file.write(string)
        i+=1
    output_file.close()
main()

