import { defineCollection, z } from 'astro:content';

const postSchema = z.object({
  title: z.string(),
  description: z.string(),
  pubDate: z.coerce.date(),
  updatedDate: z.coerce.date().optional(),
  author: z.string().default('EPM Cloud Team'),
  tags: z.array(z.string()).default([]),
  heroImage: z.string().optional(),
  draft: z.boolean().default(false),
});

export const collections = {
  'epm-updates-tutorials': defineCollection({ type: 'content', schema: postSchema }),
  'epm-updates-tips':      defineCollection({ type: 'content', schema: postSchema }),
  'epm-updates-usecases':  defineCollection({ type: 'content', schema: postSchema }),
  'epm-updates-releases':  defineCollection({ type: 'content', schema: postSchema }),

  'narrative-reporting-tutorials': defineCollection({ type: 'content', schema: postSchema }),
  'narrative-reporting-tips':      defineCollection({ type: 'content', schema: postSchema }),
  'narrative-reporting-usecases':  defineCollection({ type: 'content', schema: postSchema }),
  'narrative-reporting-releases':  defineCollection({ type: 'content', schema: postSchema }),

  'planning-cloud-tutorials': defineCollection({ type: 'content', schema: postSchema }),
  'planning-cloud-tips':      defineCollection({ type: 'content', schema: postSchema }),
  'planning-cloud-usecases':  defineCollection({ type: 'content', schema: postSchema }),
  'planning-cloud-releases':  defineCollection({ type: 'content', schema: postSchema }),
};