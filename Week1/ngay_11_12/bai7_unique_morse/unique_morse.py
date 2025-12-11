class Solution:
    def unique_morse_m(self, words):
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]

        unique_codes = set()

        for w in words:
            morse_word = ""

            for ch in w:
                index = ord(ch) - ord('a')
                morse_code = morse[index]
                morse_word = morse_word + morse_code

            # đây nè, cái chỗ này quan trọng nhất
            unique_codes.add(morse_word)

        print(unique_codes)
        return len(unique_codes)
