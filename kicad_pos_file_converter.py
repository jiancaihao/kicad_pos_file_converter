import csv, sys

def kicad_pos_convert(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as fin, \
         open(output_file, 'w', newline='', encoding='utf-8') as fout:

        writer = csv.writer(fout)
        # the title line
        writer.writerow(['Designator','Footprint','Mid X','Mid Y','Ref X','Ref Y','Pad X','Pad Y','Layer','Rotation','Comment'])
        # following a blank line
        writer.writerow(['']*11)

        for line in fin:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            # split the fields
            parts = line.split()
            if len(parts) != 7:
                continue
            ref, val, package, posx, posy, rot, side = parts

            # output line fields
            output_row = [
                ref,
                package,
                f"{posx}mm",
                f"{posy}mm",
                '', '', '', '',  # filled some blank fields
                side,
                str(int(float(rot))),  # rotation in integer type
                val
            ]
            writer.writerow(output_row)

# the main function
if __name__ == "__main__":
    # input filepath and output file path
    # for example, the input 'board.pos' with the output 'board.pos.csv'
    # the command would be:
    #    python kicad_pos_file_converter.py board.pos board.pos.csv
    if len(sys.argv) != 3:
        print("Usage: python kicad_pos_file_converter.py <input_pos_file> <output_pos_file>")
        sys.exit(1)
    input_pos = sys.argv[1]
    output_pos = sys.argv[2]

    try:
        kicad_pos_convert(input_pos, output_pos)
        print(f"Conversion completed successfully. Input file: {input_pos}, Output file: {output_pos}")
    except Exception as e:
        print(f"Error during conversion: {e}")
