import Link from 'next/link';

export default () => (
    <div>
        <h1>Portfolio</h1>
        <ul>
            <li><Link href='/portfolio/Python'><a>Python</a></Link></li>
            <li><Link href='/portfolio/JavaScript'><a>JavaScript</a></Link></li>
            <li><Link href='/portfolio/Flask'><a>Flask</a></Link></li>
            <li><Link href='/portfolio/React'><a>React</a></Link></li>
            <li><Link href='/portfolio/Next.js'><a>Next.js</a></Link></li>
        </ul>
        <a href='/'>Home</a>
        <Link href='/blog'><a>Blog</a></Link>
        <Link href='/portfolio'><a>Portfolio</a></Link>
        <Link href='/about'><a>About</a></Link>
    </div>
);