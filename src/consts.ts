// Place any global data in this file.
// You can import this data from anywhere in your site by using the `import` keyword.

export const SITE_TITLE = 'Oracle EPM Cloud Blog';
export const SITE_DESCRIPTION =
	'Tutorials, tips, use cases, and latest releases for Oracle EPM Cloud products including EPM Cloud Updates, Narrative Reporting, and Planning Cloud.';

export const PRODUCTS = [
	{
		name: 'EPM Cloud Updates',
		slug: 'epm-cloud-updates',
		description:
			'Stay current with the latest EPM Cloud platform updates, patches, and feature announcements.',
	},
	{
		name: 'Narrative Reporting',
		slug: 'narrative-reporting',
		description:
			'Explore Oracle Narrative Reporting for financial and management reporting, including report packages, bursting, and more.',
	},
	{
		name: 'Planning Cloud',
		slug: 'planning-cloud',
		description:
			'Discover Oracle Planning Cloud capabilities for budgeting, forecasting, and strategic planning.',
	},
] as const;

export const SUBCATEGORIES = [
	{ name: 'Tutorials', slug: 'tutorials', description: 'Step-by-step guides and walkthroughs' },
	{ name: 'Tips', slug: 'tips', description: 'Quick tips and best practices' },
	{ name: 'Use Cases', slug: 'use-cases', description: 'Real-world implementation examples' },
	{
		name: 'Latest Release',
		slug: 'latest-release',
		description: 'What is new in the latest release',
	},
	{
		name: 'Previous Releases Summary',
		slug: 'previous-releases-summary',
		description: 'Summary and archive of past EPM Cloud releases',
	},
	{
		name: 'EPM Cloud Platform',
		slug: 'epm-cloud-platform',
		description: 'Core platform features, architecture, and capabilities',
	},
] as const;

export type ProductSlug = (typeof PRODUCTS)[number]['slug'];
export type SubcategorySlug = (typeof SUBCATEGORIES)[number]['slug'];

/** Product-specific subcategory ordering */
export const PRODUCT_SUBCATEGORIES: Record<ProductSlug, SubcategorySlug[]> = {
	'epm-cloud-updates': ['latest-release', 'previous-releases-summary', 'epm-cloud-platform', 'tutorials'],
	'narrative-reporting': ['tutorials', 'tips', 'use-cases', 'latest-release'],
	'planning-cloud': ['tutorials', 'tips', 'use-cases', 'latest-release'],
};

/** Helper: get the full subcategory objects for a given product */
export function getSubcategoriesForProduct(productSlug: ProductSlug) {
	const slugs = PRODUCT_SUBCATEGORIES[productSlug];
	return slugs.map((s) => SUBCATEGORIES.find((sub) => sub.slug === s)!);
}
