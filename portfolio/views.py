from django.shortcuts import render

def home(request):
    context = {
        'summary': {
            'content': 'Motivated Full-Stack Python Developer with expertise in Django, Frappe, and React. Skilled in Python scripting, automation, and secure backend development. Passionate about building scalable web applications and optimizing cybersecurity protocols. Strong problem-solving abilities and hands-on experience in secure routing optimization using machine learning techniques.'
        },
        'technical_skills': [
            {'name': '🐍 Python'},
            {'name': '⚙️ Django'},
            {'name': '🖥️ Frappe'},
            {'name': '⚛️ React'},
            {'name': '💨 Tailwind CSS'},
            {'name': '🧪 Selenium'},
            {'name': '📜 JavaScript'},
            {'name': '🌿 Git'},
            {'name': '🔗 REST API'},
            {'name': '🐬 MySQL'},
            {'name': '📄 HTML'},
            {'name': '🎨 CSS'},
            {'name': '📊 Pandas'},
            {'name': '📈 NumPy'},
        ],
        'soft_skills': [
            {'name': '🗣️ Communication'},
            {'name': '🤝 Teamwork'},
            {'name': '🧠 Problem Solving'},
            {'name': '🌍 Adaptability'},
            {'name': '⏰ Time Management'},
        ],
       'projects': [
        {
    'title': 'Portfolio using Django',
    'description': [
        'Developed a personal portfolio website using Django framework.',
        'Displayed dynamic content like projects, education, skills, and certificates.',
        'Implemented Django views and models to manage and render portfolio data.',
        'Used Tailwind CSS to create a modern, responsive UI design.',
        'Integrated animation effects for smooth user experience.',
        'Enabled project listing from backend dynamically using Python and Django templating.',
        'Deployed locally and ready for production hosting.',
        'Optimized for clean code structure, maintainability, and responsiveness.'
    ],
    'github_link': 'https://github.com/Tamilarasan2002-creator/Django-portfolio'
},
{
        'title': 'My Portfolio using React',
        'description': [
            'Designed and developed a personal portfolio website using React.',
            'Showcases technical skills, projects, education, certificates, and experience.',
            'Implemented reusable React components for better code structure and scalability.',
            'Integrated Tailwind CSS for responsive and visually appealing UI design.',
            'Animated sections using AOS (Animate On Scroll) library for smooth user experience.',
            'Deployed the portfolio on Vercel with GitHub for seamless CI/CD workflow.',
            'Optimized for performance, responsiveness, and SEO.'
        ],
        'github_link': 'https://github.com/Tamilarasan2002-creator/Portfolio'
    },

{
        'title': 'ToDo List using Django',
        'description': [
            'Built a simple and user-friendly To-Do List web application using Django.',
            'Implemented CRUD operations (Create, Read, Update, Delete) for task management.',
            'Used Django\'s template system and views to handle user interactions efficiently.',
            'Integrated Tailwind CSS for a modern, responsive UI layout.',
            'Added task status toggle (completed/pending) and due-date functionality.',
            'Designed models and forms to store and validate task data.',
            'Deployed locally with development-friendly settings for testing and debugging.'
        ],
        'github_link': 'https://github.com/Tamilarasan2002-creator/To-Do-List'
    },

    {
    'title': 'Webpage for Regent using React with Tailwindcss',
    'description': [
        'Designed and developed a static webpage for Regent company using React.',
        'Created reusable components for clean and maintainable code.',
        'Implemented responsive design using Tailwind CSS.',
        'Ensured cross-browser compatibility and optimized for performance.',
        'Deployed the project on Vercel for easy access and sharing.'
    ],
    'github_link': 'https://github.com/Tamilarasan2002-creator/daily-task'
},
    {
        'title': 'Pelican Optimization Algorithm for Enhancing Mobile Secure Routing',
        'description': [
            'Focused on improving security in Wireless Sensor Networks (WSNs).',
            'Used a customized Pelican Optimization Algorithm (POA).',
            'Enhanced secure routing and intrusion detection.',
            'Implemented machine learning for attack detection.',
            'Developed using Python and network simulation tools.',
            'Integrated Python scripting for real-time monitoring.',
            'Optimized security parameters for improved IDS accuracy.',
            'Simulated and tested WSN frameworks for security robustness.'
        ],
        'github_link': 'https://github.com/yourusername/poa-secure-routing'
    },
],


        'certificates': [
            {'title': 'HTML,CSS,JavaScript', 'issued_by': 'Infosys'},
            {'title': 'Introduction of CyberSecurity', 'issued_by': 'Network Security'},
            {'title': '2nd IEEE International Conference on Data Science and Network Security (ICDSNS - 2024)', 'issued_by': ' Kalpataru Institute of Technology'},
            {'title': 'Typewriting English Junior (FIRST CLASS WITH DISTINCTION)', 'issued_by': 'Government Of Tamil Nadu'},
        ],  
        'education': [
    {
        'degree': 'B.E CyberScsurity',
        'institution': 'Mahendra Engineering College, Tamil Nadu',
        'year': '2024',
        'score': '8.3 CGPA',
        'details': [
            'Specialized in Web Development and Network Security.',
            'Completed final year project on Wireless Sensor Networks using POA.',
        ]
    },
    {
        'degree': 'HSC (Class 12)',
        'institution': 'St.marys Her Sec School',
        'year': '2020',
        'score': '68%',
        'details': [
            'Studied Computer Science and Mathematics stream.',
            'School topper in Computer Science.'
        ]
    },
    {
        'degree': 'SSLC (Class 10)',
        'institution': 'St.marys Her Sec School',
        'year': '2018',
        'score': '78%',
        'details': [
            'Scored full marks in Mathematics.',
            'Active in cultural and tech events.'
        ]
    }
],

        'experience': [
    {
        'position': 'FullStack Python Developer',
        'company': 'Regent Info Solution',
        'description': [
            'Developed and customized applications within the Frappe framework using Python scripting and automation to improve business processes.',
            'Designed and optimized billing software screens and reports, enhancing system efficiency by 20% through optimized queries and automation.',
            'Created and deployed Python-based REST APIs for seamless data exchange between different modules.',
            'Improved database performance using SQL queries, reducing query execution time by 30%.',
            'Automated routine business operations like invoice generation, reporting, and data validation using Frappe’s server-side scripting and scheduler events, increasing operational efficiency and reducing human errors.'
        ]
    },
],

   'contact': {
        'name': 'Tamilarasan',
        'email': 'tamilvrt2002@gmail.com',
        'phone': '+91 9597637510',
        'location': 'Tamil Nadu, India',
        'linkedin': 'https://www.linkedin.com/in/tamilarasan-s-40037b306/',
        'github': 'https://github.com/Tamilarasan2002-creator',
    }
    }
    return render(request, 'home.html', context)   

