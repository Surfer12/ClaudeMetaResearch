# CLAUDE.md - Project Guidelines

## Build/Run Commands
- `npm run dev` - Start development server with Wrangler
- `npm run deploy` - Deploy with Wrangler
- `npm run cf-typegen` - Generate types with Wrangler
- `cargo run` - Run Rust application
- For tests: `npx vitest` or `npx vitest run test/path/to/file.spec.ts` for a single test

## Code Style Guidelines
- **TypeScript**: Strict mode, use proper typing from `zod` for validation
- **Formatting**: ESNext, follow existing indentation (2 spaces)
- **Imports**: Group by external libraries first, then internal modules
- **Naming**: camelCase for variables/functions, PascalCase for types/interfaces/classes
- **Error Handling**: Use try/catch with proper error typing
- **API Structure**: 
  - Use Hono for API routes
  - Validate inputs with zod schemas from types.ts
  - Structure endpoints in separate files in the endpoints/ directory
- **Rust**: Follow standard Rust formatting and idioms (2018 edition)