/**
 * @file middleware.ts
 * @description manages the access to private routes
 * @version 1.0
 * @author Siddique Muhammad
 */

/**
 * Imports
 */
import { NextResponse } from "next/server";
import type { NextRequest } from 'next/server'
import cookie from 'cookie';

/**
 * @function middleware
 * @description manages the private access routes
 * @param request petition from the client
 * @returns function
 */
export function middleware(request: NextRequest) {
  const parsedCookies = cookie.parse(request.headers.get('cookie') || '');
  let logged = parsedCookies.loggedin;

  // No access to corpus/documents/search page if not logged in
  if (!logged && request.nextUrl.pathname.startsWith('/corpus')||(!logged && request.nextUrl.pathname.startsWith('/documents'))||(!logged && request.nextUrl.pathname.startsWith('/search'))) {
    return NextResponse.rewrite(new URL('/login', request.url));
  }

  // No access to login or register pages if logged in
  if (logged && (request.nextUrl.pathname.startsWith('/login') || request.nextUrl.pathname.startsWith('/register'))) {
    return NextResponse.rewrite(new URL('/', request.url));
  }

  // // Restrict access to other profile pages if logged in
  // if (userId && request.nextUrl.pathname.startsWith('/corpus/')) {
  //   const currentProfileId = request.nextUrl.pathname.split('/')[2];
  //   if (currentProfileId !== userId) {
  //     return NextResponse.redirect(new URL(`/corpus/${userId}`, request.url));
  //   }
  // }
}


// For more information:
// https://nextjs.org/docs/advanced-features/middleware