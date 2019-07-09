import { useRouter } from 'next/router';
import Link from 'next/link';

export default () => {
    const router = useRouter()
    const { entry } = router.query
    return (
        <div>
            <h1>Portfolio: { entry }</h1>
            <p>Lorem ipsum dolor sit amet...</p>
            <a href='/'>Home</a>
            <Link href='/blog'><a>Blog</a></Link>
            <Link href='/portfolio'><a>Portfolio</a></Link>
            <Link href='/about'><a>About</a></Link>
        </div>
    );
};
