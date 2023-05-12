import NavBar from "@/components/navbar";
import { useRouter } from "next/router";
function Page() {
  const router = useRouter();
  return (
    <div>
      <NavBar />
      <div></div>
    </div>
  );
}

export default Page;
