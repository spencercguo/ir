def main():
	with open('dftb_h2o_run-1-1.ener', mode='r+') as inp, open('dftb-h2o-run-clean.ener', mode='w') as out:
		out.write(inp.readline())

		lines = inp.readlines()
		prev = int(lines[0].split()[0])

		for line in lines:
			curr = int(line.split()[0])
			if prev > curr:
				num_lines_delete = prev - curr + 1
				print(num_lines_delete)
				del lines[curr:curr+num_lines_delete]
				print(lines[curr+num_lines_delete])

			prev = curr

			out.write(line)

if __name__ == '__main__':
	main()