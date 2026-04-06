import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const articles = defineCollection({
	loader: glob({ base: './src/content/articles', pattern: '**/*.{md,mdx}' }),
	schema: ({ image }) =>
		z.object({
			title: z.string(),
			description: z.string(),
			product: z.enum(['epm-cloud-updates', 'narrative-reporting', 'planning-cloud']),
			subcategory: z.enum(['tutorials', 'tips', 'use-cases', 'latest-release', 'previous-releases-summary', 'epm-cloud-platform']),
			pubDate: z.coerce.date(),
			updatedDate: z.coerce.date().optional(),
			heroImage: z.optional(image()),
		}),
});

export const collections = { articles };
