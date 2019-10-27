from Spoken_to_Written.processing_text import process



def read_and_process(path):
    r = open(path)

    for i in r:
        i = i.strip()
        p = process(i)
        print(" ".join(p))

    r.close()
