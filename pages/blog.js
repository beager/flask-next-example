import Link from 'next/link';

export default () => (
    <div>
        <h1>Marketing Page</h1>
        <a href='/'>Home</a>
        <Link href='/blog'><a>Blog</a></Link>
        <Link href='/portfolio'><a>Portfolio</a></Link>
        <Link href='/about'><a>About</a></Link>
    </div>
);