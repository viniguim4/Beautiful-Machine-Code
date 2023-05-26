##      dBBBBb dBBBBBb    dBP dBBBBb       dBP dBP dBBBBP
##     dB          dBP           dBP        dbdBP dBP.BP 
##    dB dBBB  dBBBBK   dBP dBP dBP         dBBP dBP.BP 
##   dB   BB  dBP  BB  dBP dBP dBP dBBBBBP  dBP dBP.BP  
##  dBBBBBB  dBP  dB  dBP dBP dBP          dBP dBBBBP  

with open('binary_to_btf.txt', 'rb') as f:
  data = f.read()

chunk_size = 33
chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

formatted_chunks = []
for i, chunk in enumerate(chunks):
  chunk_str = chunk.decode().strip()  # Remove 'b' prefix and newline character
  formatted_chunks.append(f'  {i} =>     "{chunk_str}",')

formatted_chunks_string = '(\n' + '\n'.join(
  formatted_chunks) + '\n  others =>     X"00000000");'

print(formatted_chunks_string)
