employ_dict = {
    'What is the term for a document that outlines a person\'s work experience, skills, and qualifications?': 'Resume',
    'In which country was the concept of the 9-to-5 workday first introduced?': 'United States',
    'What is the federal minimum wage in the United States as of 2021?': '$7.25 per hour',
    'What does the acronym "CEO" stand for?': 'Chief Executive Officer',
    'What type of employment involves working for several employers on a temporary or project basis?': 'Freelance work',
    'Who is responsible for enforcing workplace safety and health regulations in the United States?': 'Occupational Safety and Health Administration',
    'What is the term for a formal meeting between an employee and their supervisor to discuss performance and goals?': 'Performance review',
    'What term describes the voluntary termination of employment by an employee?': 'Resignation',
    'Which department in a company is typically responsible for recruiting, hiring, and managing employees?': 'Human Resources',
    'In what industry would you find someone working as a sommelier?': 'Hospitality and restaurants',
    'What law in the United States prohibits employment discrimination based on race, color, religion, sex, or national origin?': 'Civil Rights Act of 1964',
    'What is the process of finding and attracting potential job candidates called?': 'Recruitment',
    'What is the federal agency responsible for collecting labor market data and statistics in the United States?': 'Bureau of Labor Statistics',
    'What type of interview involves asking a job candidate about how they handled specific situations in the past?': 'Behavioral interview',
    'What is the term for the process of leaving a job to start one\'s own business?': 'Entrepreneurship',
    'In which industry would you find someone working as a flight attendant?': 'Aviation',
    'What is the term for the act of leaving one job to take another within the same company?': 'Internal transfer',
    'Which federal agency in the United States enforces laws related to fair labor standards and workplace conditions?': 'Wage and Hour Division',
    'What is the federal minimum wage for tipped employees in the United States as of 2021?': '$2.13 per hour',
    'What term is used for a worker who is hired on a temporary basis to cover another employee\'s absence?': 'Temp Worker',
    'What does "WFH" stand for in the context of remote work?': 'Work From Home',
    'What is the legal process for resolving disputes between employees and employers outside of the court system?': 'Arbitration',
    'What is the practice of reducing a company\'s workforce to cut costs called?': 'Downsizing',
    'What is the term for a financial incentive paid to an employee for meeting or exceeding their performance goals?': 'Commission',
    'In the context of employment, what does "I-9" refer to?': 'Employment Eligibility Verification Form',
    'In which industry would you find someone working as a geologist?': 'Earth Sciences and Mining',
    'What is the term for the act of quitting a job suddenly and without notice?': 'Job abandonment',
    'What is the term for a form of discrimination that occurs when an employee is treated unfairly due to their age?': 'Ageism',
    'What is the practice of providing employees with opportunities to develop new skills and advance their careers within the company?': 'Employee development',
    'In which industry would you find someone working as a veterinarian?': 'Veterinary Medicine',
    'Which skill is often described as the ability to understand and manage your own emotions and those of others?': 'Emotional intelligence',
    'What is the term for the ability to solve problems and make decisions quickly and effectively?': 'Critical thinking',
    'What type of skill is typically associated with the ability to speak effectively and persuasively?': 'Communication skills',
    'What is the process of setting specific, measurable, achievable, relevant, and time-bound goals known as?': 'Goal setting',
    'Which skill involves the ability to adapt to new situations and challenges?': 'Adaptability',
    'What term is often used to describe the ability to work effectively with others in a team setting?': 'Collaboration',
    'What is the ability to identify and manage your own stress and that of others called?': 'Stress management',
    'Which skill involves the ability to identify and analyze problems and develop solutions?': 'Problem-solving',
    'Which skill is crucial for understanding and navigating the digital world and technology?': 'Digital literacy',
    'Which skill involves the ability to write clearly and persuasively?': 'Writing skills',
    'In the context of skill development, what does "PDCA" stand for?': 'Plan-Do-Check-Act',
    'Which skill is crucial for understanding and managing cultural differences in a global context?': 'Cultural competence',
    'What term is used for the ability to think creatively and generate innovative ideas?': 'Creativity',
    'What is the ability to understand and manage conflicts in a constructive manner called?': 'Conflict resolution',
    'What is the ability to deliver compelling and persuasive presentations known as?': 'Presentation skills',
    'What profession involves the repair and maintenance of electrical systems in buildings?': 'Electrician',
    'What is the branch of engineering that deals with the design and construction of structures?': 'Civil Engineering',
    'What is the profession that focuses on creating and styling hair and makeup for clients?': 'Cosmetology',
    'Which career field specializes in diagnosing and treating diseases through medical imaging?': 'Radiology',
    'In the culinary arts, what do we call a chef who specializes in desserts and pastries?': 'Pastry Chef'
}

employ_ans_dict = {'Resume': ['Resume', 'Curriculum Vitae', 'Bio-data', 'Job Application'],
                   'United States': ['United States', 'United Kingdom', 'Canada', 'Germany'],
                   '$7.25 per hour': ['$7.25 per hour', '$7.00 per hour', '$8.50 per hour', '$9.00 per hour'],
                   'Chief Executive Officer': ['Chief Executive Officer', 'Corporate Executive Officer', 'Chief Executive Organizer', 'Central Executive Officer'],
                   'Freelance work': ['Freelance work', 'Full-time employment', 'Permanent work', 'Part-time job'],
                   'Occupational Safety and Health Administration': ['Occupational Safety and Health Administration', 'Department of Labor', 'Workplace Safety Bureau', 'Federal Safety Commission'],
                   'Performance review': ['Performance review', 'Employee appraisal', 'Progress assessment', 'Job evaluation'],
                   'Resignation': ['Resignation', 'Departure', 'Withdrawal', 'Termination'],
                   'Human Resources': ['Human Resources', 'Employment Division', 'Workforce Operations', 'Personnel Management'],
                   'Hospitality and restaurants': ['Hospitality and restaurants', 'Information Technology', 'Agriculture and Farming', 'Construction and Engineering'],
                   'Civil Rights Act of 1964': ['Civil Rights Act of 1964', 'Equal Pay Act of 1963', 'Fair Labor Standards Act of 1938', 'Employment Non-Discrimination Act'],
                   'Recruitment': ['Recruitment', 'Talent Harvesting', 'Staffing Procurement', 'Job Seeker Gathering'],
                   'Bureau of Labor Statistics': ['Bureau of Labor Statistics', 'Department of Labor Statistics', 'Labor Market Bureau', 'Employment Statistics Agency'],
                   'Behavioral interview': ['Behavioral interview', 'Experience-based interview', 'Situational interview', 'Scenario-based interview'],
                   'Entrepreneurship': ['Entrepreneurship', 'Freelancing', 'Career change', 'Self-employment'],
                   'Aviation': ['Aviation', 'Marine Biology', 'Retail', 'Agriculture'],
                   'Internal transfer': ['Internal transfer', 'Intra-company shift', 'Internal promotion', 'Workplace transition'],
                   'Wage and Hour Division': ['Wage and Hour Division', 'Labor Standards Bureau', 'Employment Compliance Agency', 'Workplace Regulations Division'],
                   '$2.13 per hour': ['$2.13 per hour', '$3.50 per hour', '$4.75 per hour', '$2.00 per hour'],
                   'Temp Worker': ['Temp Worker', 'Stand-in Employee', 'Replacement Worker', 'Substitute Staff'],
                   'Work From Home': ['Work From Home', 'Weekend Fun Hub', 'Wireless File Hosting', 'Workforce Handshake'],
                   'Arbitration': ['Arbitration', 'Workplace Mediation', 'Labor Negotiation', 'Employee Tribunal'],
                   'Downsizing': ['Downsizing', 'Right-sizing', 'Staff optimization', 'Workforce streamlining'],
                   'Commission': ['Commission', 'Bonus', 'Salary', 'Stipend'],
                   'Employment Eligibility Verification Form': ['Employment Eligibility Verification Form', 'Work Authorization Form', 'Employee Identification Document', 'Job Application Record'],
                   'Earth Sciences and Mining': ['Earth Sciences and Mining', 'Fashion', 'Culinary Arts', 'Film Production'],
                   'Job abandonment': ['Job abandonment', 'Sudden Departure', 'Unplanned Resignation', 'Workforce Exit'],
                   'Ageism': ['Ageism', 'Age Discrimination', 'Age Bias', 'Generational Discrimination'],
                   'Employee development': ['Employee development', 'Employee enrichment', 'Career expansion', 'Workforce progress'],
                   'Veterinary Medicine': ['Veterinary Medicine', 'Accounting', 'Fashion Design', 'Aerospace Engineering'],
                   'Emotional intelligence': ['Emotional intelligence', 'Empathy', 'Emotional awareness', 'Social intelligence'],
                   'Critical thinking': ['Critical thinking', 'Rapid resolution', 'Instinctive judgment', 'Swift problem-solving'],
                   'Communication skills': ['Communication skills', 'Verbal proficiency', 'Rhetorical expertise', 'Dialogue aptitude'],
                   'Goal setting': ['Goal setting', 'Objective establishment', 'Target definition', 'Ambition outlining'],
                   'Adaptability': ['Adaptability', 'Flexibility', 'Versatility', 'Agility'],
                   'Collaboration': ['Collaboration', 'Teamwork', 'Cooperation', 'Group synergy'],
                   'Stress management': ['Stress management', 'Stress control', 'Stress handling', 'Stress moderation'],
                   'Problem-solving': ['Problem-solving', 'Issue resolution', 'Dilemma analysis', 'Challenge tackling'],
                   'Digital literacy': ['Digital literacy', 'Digital Archeology', 'Binary Coding', 'Technomics'],
                   'Writing skills': ['Writing skills', 'Graphite Artistry', 'Verbal Dexterity', 'Narrative Juggling'],
                   'Plan-Do-Check-Act': ['Plan-Do-Check-Act', 'Perfectly-Defined-Comprehensive-Analysis', 'Produce-Distribute-Consume-Adjust', 'Prevent Disaster-Control Actions'],
                   'Cultural competence': ['Cultural competence', 'Geographical knowledge', 'Culinary experience', 'Mathematical proficiency'],
                   'Creativity': ['Creativity', 'Originality', 'Imagination', 'Invention'],
                   'Conflict resolution': ['Conflict resolution', 'Conflict avoidance', 'Conflict escalation', 'Conflict creation'],
                   'Presentation skills': ['Presentation skills', 'Communication Skills', 'Speaking Skills', 'Public Speaking Skills'],
                   'Electrician': ['Electrician', 'Painter', 'Construction', 'Engineering'],
                   'Civil Engineering': ['Civil Engineering','Mechanical Engineering', 'Electrical Engineering', 'Aerospace Engineering'],
                   'Cosmetology': ['Cosmetology', 'prosthetics', 'Special Effects Makeup Artist', 'Costume Designer'],
                   'Radiology': ['Radiology', 'Sonography', 'Nuclear Medicine', 'Neuroscience'],
                   'Pastry Chef': ['Pastry Chef', 'Sous-chef', 'Commis Chef', 'Chef de partie']
                   }
