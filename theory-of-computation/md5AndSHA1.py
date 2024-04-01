import hashlib

# Read a hash md5 separete hash in 4 parts, these 4 parts are words, and cocatenate to create 2 words with the hash

def compute_md5(input_string):
    return hashlib.md5(input_string.encode()).hexdigest()

def compute_sha1(input_string):
    return hashlib.sha1(input_string.encode()).hexdigest()

def split_and_concat_md5(md5_hash):
    # Split the MD5 hash into 4 parts
    part1 = md5_hash[:8]
    part2 = md5_hash[8:16]
    part3 = md5_hash[16:24]
    part4 = md5_hash[24:]

    print(f"Word 1: {part1}\nWord 2: {part2}\nWord 3: {part3}\nWord 4: {part4}")
  
    # Concatenate parts 1 and 3, and parts 2 and 4
    concatenated_part1_3 = part1 + part3
    concatenated_part2_4 = part2 + part4

    return concatenated_part1_3, concatenated_part2_4

def split_and_concat_sha1(sha1_hash):
    # Split the SHA1 hash into 4 parts
    part1 = sha1_hash[:10]
    part2 = sha1_hash[10:20]
    part3 = sha1_hash[20:30]
    part4 = sha1_hash[30:]

    print(f"Word 1: {part1}\nWord 2: {part2}\nWord 3: {part3}\nWord 4: {part4}")
  
    # Concatenate parts 1 and 3, and parts 2 and 4
    concatenated_part1_3 = part1 + part3
    concatenated_part2_4 = part2 + part4

    return concatenated_part1_3, concatenated_part2_4

def main():
    input_hash = input("Enter the hash: ")

    if len(input_hash) <= 32:
        md5_hash = compute_md5(input_hash)
        print("MD5 hash:", md5_hash)
        result = split_and_concat_md5(md5_hash)
        print("\nConcatenated Word 1 with Word 3:", result[0])
        print("Concatenated Word 2 with Word 4:", result[1])
    else:
        sha1_hash = compute_sha1(input_hash)
        print("SHA1 hash:", sha1_hash)
        result = split_and_concat_sha1(sha1_hash)
        print("\nConcatenated Word 1 with Word 3:", result[0])
        print("Concatenated Word 2 with Word 4:", result[1])

if __name__ == "__main__":
    main()