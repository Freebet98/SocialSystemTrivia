language_dict = {'How many writing systems does the Japanese Language Use?': 'Three',
                 'What does the Latin Phrase “quid pro quo” mean?': 'Something for something',
                 'What are the two most common languages spoken in South America?': 'Spanish and Portuguese',
                 'What area of study, signifies the “art of technique of arranging type to make written language legible, readable, and appealing?': 'Typography',
                 'What language, other than English, is additionally spoken in Quebec Canada?': 'French',
                 'What is the additional word meaning “you” that is used in Spain Spanish?': 'Vosotros',
                 'What is the hardest language to learn?': 'Mandarin Chinese',
                 'How many dialects are there in the Philippines?': '111',
                 'Which of these traditional languages can be read bottom to top?': 'Berber',
                 'What language has the longest alphabet?': 'Khmer/Cambodian',
                 'Rotokas is believed to have the smallest alphabet, with 12 letters. Where does it originate?': 'Papua New Guinea',
                 'What is the language that all the Romance languages derive from?': 'Latin',
                 'The Tai language family is made up of two groups, Tai & Kadai. What countries most commonly use this?': 'Thailand & Laos',
                 'What region or group of people developed the original English alphabet?': 'Phoenicians',
                 'What writing system is known for being stylized pictures of objects, or symbols to represent meaning?': 'Hieroglyphics',
                 'What are the two languages spoken in Finland?': 'Finnish and Swedish',
                 'The old English alphabet only had 23 letters, what are the 3 missing letters?': 'J, U, W',
                 'What language of Polynesian descent, is commonly used in certain parts of the US?': 'Hawaiian',
                 'The prefix “Minne” is part of many names in Minnesota. Deriving from the Dakota language, what does it mean?': 'Water',
                 'Which of the following is not considered a Romance language?': 'English',
                 'Wolof, Yoruba, Sotho, San, and Xhosa are all languages spoken primarily on what continent?': 'Africa',
                 'What country in South America, has its official language as Dutch?': 'Suriname',
                 'Countries in Africa like Angola, Mozambique, Equatorial Guinea, and Cape Verde all share an official language with Brazil, what language is it?': 'Portugese',
                 'What is the ~ (squiggle) accent you see on letters, such as ñ, called?': 'Tilde',
                 'Math is said to have its own language, which of the following is not a type of number system?': 'Centennial',
                 'What are the 6 official languages of the United Nations? Which of the following is not an official language of the United Nations?': 'Hindi',
                 'Hangul is the official language of which religion in East Asia?': 'Korea',
                 'Which of the following is not one of the top 5 most common languages English is a combination of?': 'Celtic',
                 'When did Webster publish his first dictionary? ': '1806',
                 'How many countries do not have an official language?': '5',
                 'English is the third most commonly spoken language in the world. How many countries is English the official language of?': '67',
                 'According to Historians and linguists, which of the following is not one of the 3 oldest languages to exist with clear written records?': 'Etruscan',
                 'What is the oldest living language?': 'Tamil',
                 'What is the most spoken indigenous language used in the US?': 'Navajo',
                 'In addition to French, what is the official language of Madagascar?': 'Malagasy',
                 'How many countries have French as their official language?': '29',
                 'What is the name of the language, or number system used to represent computer processor instructions?': 'Binary',
                 'What is the form of communication depicted by dots and dashes?': 'Morse Code',
                 'How many countries around the world have a recognized sign language system?': '41',
                 'What is the study of language called?': 'Linguistics',
                 'Sumerian language is one of the oldest languages in past existence, attesting to what BCE?': '3100 BCE',
                 'It is believed that the first spoken word was “Aa”, from the australopithecine in Ethiopia, what did it mean or refer to?': 'Hey',
                 'What is the only African Nation to have an official language of Spanish?': 'Equatorial Guinea',
                 'What word means “Library” in at least three Romance languages, including Portuguese, Spanish, and Italian?': 'Biblioteca',
                 'Which of the following is not amongst the top 7 studied languages in the world?': 'Korean',
                 'How do you write "Cat" in Morse code?': '-. -.. --',
                 'What is the official language of Brazil?': 'Portuguese',
                 'Which country is often referred to as the "Land of the Rising Sun"?': 'Japan',
                 'In economics, what does "LDC" stand for?': 'Less Developed Country',
                 'Who developed the concept of the "invisible hand" in economics, which describes how self-interested individuals can unintentionally promote the collective good?': 'Adam Smith'
                 }

language_ans_dict = {'Three': ['Three', 'Five', 'One', 'Four'],
                     'Something for something': ['Something for something', 'It is what it is', 'An arm for a leg',
                                                 'An eye for an eye'],
                     'Spanish and Portuguese': ['Spanish and Portuguese', 'Spanish and English',
                                                'English and Portuguese', 'Spanish and French'],
                     'Typography': ['Typography', 'Astrography', 'Heliowriting', 'Floraligraphy'],
                     'French': ['French', 'Quebecois', 'Canadian', 'Montagnais'],
                     'Vosotros': ['Vosotros', 'Vous', 'Voces', 'Ihr'],
                     'Mandarin Chinese': ['Mandarin Chinese', 'Navajo', 'Japanese', 'Icelandic'],
                     '111': ['111', '8', '72', '312'],
                     'Berber': ['Berber', 'Vietnamese', 'Persian', 'Sindhi'],
                     'Khmer/Cambodian': ['Khmer/Cambodian', 'Nepali', 'Hindi', 'Japanese'],
                     'Papua New Guinea': ['Papua New Guinea', 'Caledonia', 'Greater Sunda Islands', 'Falkland Islands'],
                     'Latin': ['Latin', 'Greek', 'Etruscan', 'Celtic'],
                     'Thailand & Laos': ['Thailand & Laos', 'Indonesia and Malaysia', 'Maluku and West Papua',
                                         'Sri Lanka and Burma'],
                     'Phoenicians': ['Phoenicians', 'Greeks', 'Trojans', 'Romans'],
                     'Hieroglyphics': ['Hieroglyphics', 'Petroglyphs', 'Lithoglyphs', 'Ditriglyphs'],
                     'Finnish and Swedish': ['Finnish and Swedish', 'Finnish and Icelandic', 'Finnish and Norwegian',
                                             'Finnish and English'],
                     'J, U, W': ['J, U, W', 'K, V, Y', 'G, W, Z', 'I, V, Q'],
                     'Hawaiian': ['Hawaiian', 'Samoan', 'Tahitian', 'French'],
                     'Water': ['Water', 'Cold', 'Lake', 'Snow'],
                     'English': ['English', 'Spanish', 'Latin', 'Portugese'],
                     'Africa': ['Africa', 'South America', 'Australia', 'Asia'],
                     'Suriname': ['Suriname', 'Guyana', 'Trinidad and Tobago', 'Grenada'],
                     'Portugese': ['Portugese', 'Spanish', 'English', 'French'],
                     'Tilde': ['Tilde', 'Diaeresis', 'Acute', 'Trema'],
                     'Centennial': ['Centennial', 'Binary', 'Octal', 'Decimal'],
                     'Hindi': ['Hindi', 'Russian', 'French', 'Spanish'],
                     'Korea': ['Korea', 'Japan', 'Taiwan', 'Vietnam'],
                     'Celtic': ['Celtic', 'Dutch', 'German', 'Greek'],
                     '1806': ['1806', '1796', '1821', '1901'],
                     '5': ['5', '0', '7', '9'],
                     '67': ['67', '53', '89', '92'],
                     'Etruscan': ['Etruscan', 'Sumerian', 'Akkadian', 'Egyptian'],
                     'Tamil': ['Tamil', 'Sanskrit', 'Farsi', 'Greek'],
                     'Navajo': ['Navajo', 'Ojibwe', 'Cree', 'Apache'],
                     'Malagasy': ['Malagasy', 'Portuguese', 'English', 'Bantu'],
                     '29': ['29', '33', '25', '31'],
                     'Binary': ['Binary', 'Hexadecimal', 'Base 2', 'Bit'],
                     'Morse Code': ['Morse Code', 'Semaphor', 'The Tap Code', 'Baudot Code'],
                     '41': ['41', '52', '99', '23'],
                     'Linguistics': ['Linguistics', 'Phonology', 'Etymology', 'Philology'],
                     '3100 BCE': ['3100 BCE', '2100 BCE', '1100 BCE', '4100 BCE'],
                     'Hey': ['Hey', 'No', 'Food', 'Stop'],
                     'Equatorial Guinea': ['Equatorial Guinea', 'Sao Tome', 'Gabon', 'Guinea'],
                     'Biblioteca': ['Biblioteca', 'Librairie', 'Leabhar', 'Bibliophile'],
                     'Korean': ['Korean', 'German', 'Japanese', 'Italian'],
                     '-. -.. --': ['-. -.. --', '-.- ..- -.', '..- -. .-', '-. -.. .-'],
                     'Portuguese': ['Portuguese', 'Spanish', 'Quechua', 'Dutch'],
                     'Japan': ['Japan', 'China', 'Korea', 'Tibet'],
                     'Less Developed Country': ['Less Developed Country', 'Linear Degrading Capital',
                                                'Large Domestic Consumer', 'Lesser Dominant Cashflow'],
                     'Adam Smith': ['Adam Smith', 'Tim Johnson', 'Karl Marx', 'Simon Sewell']
                     }
