   // إضافة تفاعل للعناصر
        document.querySelectorAll('.nav-item').forEach(item => {
            item.addEventListener('click', function() {
                // إزالة الفئة النشطة من جميع العناصر
                document.querySelectorAll('.nav-item').forEach(nav => nav.classList.remove('active'));
                // إضافة الفئة النشطة للعنصر المحدد
                this.classList.add('active');
            });
        });

        // تأثير تمرير الماوس على الـ header
        const header = document.querySelector('.header');
        header.addEventListener('mouseenter', () => {
            header.style.background = 'rgba(255, 255, 255, 1)';
        });
        header.addEventListener('mouseleave', () => {
            header.style.background = 'rgba(255, 255, 255, 0.95)';
        });