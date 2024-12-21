# Project Documentation

## __init__.py

## docstring_extractor.py

### Class: DocstringExtractor

Extract docstrings and type information from Python files in a directory.

#### __init__

```python
__init__(self: Any, directory: str)
```

Initialize the DocstringExtractor.

Args:
    directory (str): Path to the directory containing Python files

#### setup_logging

```python
setup_logging(self: Any)
```

Configure logging for the extractor.

#### get_python_files

```python
get_python_files(self: Any) -> List[Path]
```

Find all Python files in the directory and its subdirectories.

Returns:
    List[Path]: List of paths to Python files

#### get_type_annotation

```python
get_type_annotation(self: Any, node: Any) -> str
```

Convert AST type annotation to string representation.

Args:
    node (ast.AST): AST node containing type annotation
    
Returns:
    str: String representation of the type

#### extract_function_info

```python
extract_function_info(self: Any, node: Union[(Any, Any)]) -> Dict[(str, Any)]
```

Extract function information including docstring, arguments, and return type.

Args:
    node (Union[ast.FunctionDef, ast.AsyncFunctionDef]): Function AST node
    
Returns:
    Dict[str, Any]: Dictionary containing function information

#### extract_class_info

```python
extract_class_info(self: Any, node: Any) -> Dict[(str, Any)]
```

Extract class information including docstring and methods.

Args:
    node (ast.ClassDef): Class AST node
    
Returns:
    Dict[str, Any]: Dictionary containing class information

#### extract_docstrings_from_file

```python
extract_docstrings_from_file(self: Any, file_path: Path) -> Dict[(str, Any)]
```

Extract docstrings and type information from a single Python file.

Args:
    file_path (Path): Path to the Python file
    
Returns:
    Dict[str, Any]: Dictionary containing file information

#### extract_all_docstrings

```python
extract_all_docstrings(self: Any) -> Dict[(str, Dict[(str, str)])]
```

Extract docstrings from all Python files in the directory.

Returns:
    Dict[str, Dict[str, str]]: Dictionary mapping file paths to their docstrings

#### save_documentation

```python
save_documentation(self: Any, output_file: str)
```

Save extracted docstrings and type information as Markdown documentation.

Args:
    output_file (str): Path to the output markdown file

## docs/source/conf.py

## goodfire/__init__.py

## goodfire/exceptions.py

### Class: InferenceAbortedException

## goodfire/variants/variants.py

### Class: Variant

A class representing a variant of a base model with feature modifications.

This class allows for creating variants of a base model by applying
feature modifications through either nudging or pinning values.

Args:
    base_model (str): Identifier of the base model to create variants from

Attributes:
    base_model (str): The base model identifier
    edits (FeatureEdits): Collection of feature modifications

#### __init__

```python
__init__(self: Any, base_model: SUPPORTED_MODELS)
```

#### set

```python
set(self: Any)
```

#### clear

```python
clear(self: Any, feature: Union[(Feature, FeatureGroup)])
```

Remove modifications for specified feature(s).

Args:
    feature (Union[Feature, FeatureGroup]): Feature(s) to clear modifications for

#### reset

```python
reset(self: Any)
```

Remove all feature modifications.

#### __repr__

```python
__repr__(self: Any)
```

#### __str__

```python
__str__(self: Any)
```

#### from_json

```python
from_json(cls: Any, variant_json: Union[(str, dict)])
```

#### json

```python
json(self: Any)
```

Convert the variant to a JSON-compatible dictionary.

Returns:
    dict: Dictionary containing base model and feature configurations

#### set_when

```python
set_when(self: Any, condition: ConditionalGroup, values: Union[(FeatureEdits, dict[(Union[(Feature, FeatureGroup)], float)])]) -> None
```

#### abort_when

```python
abort_when(self: Any, condition: ConditionalGroup) -> None
```

#### handle_when

```python
handle_when(self: Any, condition: ConditionalGroup, handler: HandlerCallable) -> None
```

#### controller

```python
controller(self: Any) -> Controller
```

Get a controller instance with the variant's modifications applied.

Returns:
    Controller: Controller instance with feature modifications

### Class: NestedScope

#### __init__

```python
__init__(self: Any, condition: ConditionalGroup, base_variant: Variant, event_name: Optional[str])
```

#### json

```python
json(self: Any)
```

#### from_json

```python
from_json(cls: Any, nested_scope_json: Union[(str, dict)])
```

### Class: InferenceContext

## goodfire/variants/__init__.py

## goodfire/features/interfaces.py

## goodfire/features/__init__.py

## goodfire/features/features.py

### Class: FeatureNotInGroupError

### Class: Feature

A class representing a single feature aka a conceptual unit of the SAE.

Handles individual feature operations and comparisons. Features can be combined
into groups and compared using standard operators.

Attributes:
    uuid (UUID): Unique identifier for the feature
    label (str): Human-readable label describing the feature
    max_activation_strength (float): Maximum activation strength of the feature in the
    training dataset
    index_in_sae (int): Index position in the SAE

#### __init__

```python
__init__(self: Any, uuid: UUID, label: str, max_activation_strength: float, index_in_sae: int)
```

Initialize a new Feature instance.

Args:
    uuid: Unique identifier for the feature
    label: Human-readable label describing the feature
    max_activation_strength: Maximum activation strength of the feature
    index_in_sae: Index position in the SAE

#### json

```python
json(self: Any)
```

#### from_json

```python
from_json(data: dict[(str, Any)])
```

#### __or__

```python
__or__(self: Any, other: Feature)
```

#### __repr__

```python
__repr__(self: Any) -> str
```

#### __hash__

```python
__hash__(self: Any)
```

#### __str__

```python
__str__(self: Any)
```

#### __eq__

```python
__eq__(self: Any, other: Union[(FeatureGroup, Feature, float)]) -> Conditional
```

#### __ne__

```python
__ne__(self: Any, other: Union[(FeatureGroup, Feature, float)]) -> Conditional
```

#### __le__

```python
__le__(self: Any, other: Union[(FeatureGroup, Feature, float)]) -> Conditional
```

#### __lt__

```python
__lt__(self: Any, other: Union[(FeatureGroup, Feature, float)]) -> Conditional
```

#### __ge__

```python
__ge__(self: Any, other: Union[(FeatureGroup, Feature, float)]) -> Conditional
```

#### __gt__

```python
__gt__(self: Any, other: Union[(FeatureGroup, Feature, float)]) -> Conditional
```

### Class: FeatureGroup

A collection of Feature instances with group operations.

Provides functionality for managing and operating on groups of features, including
union and intersection operations, indexing, and comparison operations.

Example:
    >>> feature_group = FeatureGroup([feature1, feature2, feature3, feature4])
    >>> # Access single feature by index
    >>> first_feature = feature_group[0]  # Returns Feature
    >>>
    >>> # Slice features
    >>> first_two = feature_group[0:2]  # Returns FeatureGroup with features 0,1
    >>> last_two = feature_group[-2:]   # Returns FeatureGroup with last 2 features
    >>>
    >>> # Multiple indexes using list or tuple
    >>> selected = feature_group[[0, 2]]  # Returns FeatureGroup with features 0,2
    >>> selected = feature_group[0, 3]    # Returns FeatureGroup with features 0,3

#### __init__

```python
__init__(self: Any, features: Optional[list[Feature]])
```

#### __iter__

```python
__iter__(self: Any)
```

#### __getitem__

```python
__getitem__(self: Any, index: Union[(int, list[int], tuple[(int, Ellipsis)], slice)])
```

#### __repr__

```python
__repr__(self: Any)
```

#### pick

```python
pick(self: Any, feature_indexes: list[int])
```

Create a new FeatureGroup with selected features.

Args:
    feature_indexes: List of indexes to select

Returns:
    FeatureGroup: New group containing only the selected features

#### json

```python
json(self: Any) -> dict[(str, Any)]
```

#### from_json

```python
from_json(data: dict[(str, Any)])
```

#### add

```python
add(self: Any, feature: Feature)
```

Add a feature to the group.

Args:
    feature: Feature instance to add to the group

#### pop

```python
pop(self: Any, index: int)
```

Remove and return a feature at the specified index.

Args:
    index: Index of the feature to remove

Returns:
    Feature: The removed feature

#### union

```python
union(self: Any, feature_group: FeatureGroup)
```

Combine this group with another feature group.

Args:
    feature_group: Another FeatureGroup to combine with

Returns:
    FeatureGroup: New group containing features from both groups

#### intersection

```python
intersection(self: Any, feature_group: FeatureGroup)
```

Create a new group with features common to both groups.

Args:
    feature_group: Another FeatureGroup to intersect with

Returns:
    FeatureGroup: New group containing only features present in both groups

#### __or__

```python
__or__(self: Any, other: FeatureGroup)
```

#### __and__

```python
__and__(self: Any, other: FeatureGroup)
```

#### __len__

```python
__len__(self: Any)
```

#### __str__

```python
__str__(self: Any)
```

#### __eq__

```python
__eq__(self: Any, other: Union[(FeatureGroup, Feature, float)]) -> Conditional
```

#### __ne__

```python
__ne__(self: Any, other: Union[(FeatureGroup, Feature, float)]) -> Conditional
```

#### __le__

```python
__le__(self: Any, other: Union[(FeatureGroup, Feature, float)]) -> Conditional
```

#### __lt__

```python
__lt__(self: Any, other: Union[(FeatureGroup, Feature, float)]) -> Conditional
```

#### __ge__

```python
__ge__(self: Any, other: Union[(FeatureGroup, Feature, float)]) -> Conditional
```

#### __gt__

```python
__gt__(self: Any, other: Union[(FeatureGroup, Feature, float)]) -> Conditional
```

### Class: ConditionalGroup

Groups multiple conditions with logical operators.

Manages groups of conditions that can be combined using AND/OR operations.

#### __init__

```python
__init__(self: Any, conditionals: list[Conditional], operator: JOIN_OPERATOR)
```

Initialize a new ConditionalGroup.

Args:
    conditionals: List of Conditional instances to group
    operator: Logical operator to join conditions ("AND" or "OR")

#### json

```python
json(self: Any, scale: float) -> dict[(str, Any)]
```

Convert the conditional group to a JSON-serializable dictionary.

Returns:
    dict: Dictionary containing conditionals and operator

#### from_json

```python
from_json(data: dict[(str, Any)])
```

Create a ConditionalGroup instance from JSON data.

Args:
    data: Dictionary containing conditionals and operator

Returns:
    ConditionalGroup: New instance with the deserialized data

#### __and__

```python
__and__(self: Any, other: Union[(ConditionalGroup, Conditional)]) -> ConditionalGroup
```

#### __or__

```python
__or__(self: Any, other: Union[(ConditionalGroup, Conditional)]) -> ConditionalGroup
```

#### __str__

```python
__str__(self: Any)
```

#### __repr__

```python
__repr__(self: Any)
```

#### __getitem__

```python
__getitem__(self: Any, index: Union[(int, slice, tuple[(int, Ellipsis)])])
```

#### __len__

```python
__len__(self: Any)
```

#### __contains__

```python
__contains__(self: Any, item: Conditional)
```

#### __iter__

```python
__iter__(self: Any)
```

#### __mul__

```python
__mul__(self: Any, other: float)
```

#### __rmul__

```python
__rmul__(self: Any, other: float)
```

#### __truediv__

```python
__truediv__(self: Any, other: float)
```

#### __rtruediv__

```python
__rtruediv__(self: Any, other: float)
```

#### __add__

```python
__add__(self: Any, other: float)
```

#### __radd__

```python
__radd__(self: Any, other: float)
```

#### __sub__

```python
__sub__(self: Any, other: float)
```

#### __rsub__

```python
__rsub__(self: Any, other: float)
```

#### __neg__

```python
__neg__(self: Any)
```

#### __abs__

```python
__abs__(self: Any)
```

#### __pow__

```python
__pow__(self: Any, other: float)
```

#### __rpow__

```python
__rpow__(self: Any, other: float)
```

### Class: Conditional

Represents a conditional expression comparing features.

Handles comparison operations between features, feature groups, and statistics.

#### __init__

```python
__init__(self: Any, left_hand: FeatureGroup, right_hand: Union[(Feature, FeatureGroup, float)], operator: CONDITIONAL_OPERATOR)
```

Initialize a new Conditional.

Args:
    left_hand: FeatureGroup for the left side of the comparison
    right_hand: Value to compare against (Feature, FeatureGroup, or float)
    operator: Comparison operator to use

#### json

```python
json(self: Any, scale: float) -> dict[(str, Any)]
```

Convert the conditional to a JSON-serializable dictionary.

Returns:
    dict: Dictionary containing the conditional expression data

#### from_json

```python
from_json(data: dict[(str, Any)])
```

Create a Conditional instance from JSON data.

Args:
    data: Dictionary containing conditional expression data

Returns:
    Conditional: New instance with the deserialized data

#### __and__

```python
__and__(self: Any, other: Conditional) -> ConditionalGroup
```

#### __or__

```python
__or__(self: Any, other: Conditional) -> ConditionalGroup
```

#### __str__

```python
__str__(self: Any)
```

#### __repr__

```python
__repr__(self: Any)
```

#### __mul__

```python
__mul__(self: Any, other: float)
```

#### __rmul__

```python
__rmul__(self: Any, other: float)
```

#### __truediv__

```python
__truediv__(self: Any, other: float)
```

#### __rtruediv__

```python
__rtruediv__(self: Any, other: float)
```

#### __add__

```python
__add__(self: Any, other: float)
```

#### __radd__

```python
__radd__(self: Any, other: float)
```

#### __sub__

```python
__sub__(self: Any, other: float)
```

#### __rsub__

```python
__rsub__(self: Any, other: float)
```

#### __neg__

```python
__neg__(self: Any)
```

#### __abs__

```python
__abs__(self: Any)
```

#### __pow__

```python
__pow__(self: Any, other: float)
```

#### __rpow__

```python
__rpow__(self: Any, other: float)
```

### Class: FeatureEdits

#### __init__

```python
__init__(self: Any, edits: list[tuple[(Feature, float)]])
```

#### __str__

```python
__str__(self: Any)
```

#### __repr__

```python
__repr__(self: Any)
```

#### __getitem__

```python
__getitem__(self: Any, index: Union[(int, slice, tuple[(int, Ellipsis)])])
```

#### __setitem__

```python
__setitem__(self: Any, index: int, value: tuple[(Feature, float)])
```

#### set

```python
set(self: Any, feature: Feature, value: float)
```

#### remove

```python
remove(self: Any, feature: Feature)
```

#### rescale

```python
rescale(self: Any)
```

#### reset

```python
reset(self: Any)
```

#### __len__

```python
__len__(self: Any)
```

#### pop

```python
pop(self: Any, index: int)
```

#### __iter__

```python
__iter__(self: Any)
```

#### __contains__

```python
__contains__(self: Any, feature: Feature)
```

#### __eq__

```python
__eq__(self: Any, other: FeatureEdits)
```

#### __ne__

```python
__ne__(self: Any, other: FeatureEdits)
```

#### __hash__

```python
__hash__(self: Any)
```

#### __mul__

```python
__mul__(self: Any, other: float)
```

#### __rmul__

```python
__rmul__(self: Any, other: float)
```

#### __truediv__

```python
__truediv__(self: Any, other: float)
```

#### __rtruediv__

```python
__rtruediv__(self: Any, other: float)
```

#### __add__

```python
__add__(self: Any, other: float)
```

#### __radd__

```python
__radd__(self: Any, other: float)
```

#### __sub__

```python
__sub__(self: Any, other: float)
```

#### __rsub__

```python
__rsub__(self: Any, other: float)
```

#### __neg__

```python
__neg__(self: Any)
```

#### __abs__

```python
__abs__(self: Any)
```

#### __pow__

```python
__pow__(self: Any, other: float)
```

#### __rpow__

```python
__rpow__(self: Any, other: float)
```

#### as_dict

```python
as_dict(self: Any)
```

## goodfire/utils/asyncio.py

### Function: run_async_safely

```python
run_async_safely(coro: Coroutine[(Any, Any, T)]) -> T
```

Safely runs a coroutine in a sync context, handling existing event loops.

Args:
    coro: The coroutine to run

Returns:
    The result of the coroutine

## goodfire/utils/__init__.py

## goodfire/utils/edit.py

### Class: Claude

#### __init__

```python
__init__(self: Any, anthropic_api_key: str, model_name: str, backup_models: Optional[list[str]])
```

#### chat

*Async method*

```python
chat(self: Any, message_history: Any, system_prompt: Optional[str], max_tokens_to_sample: int, temperature: float, max_retries: int)
```

### Class: LanguageModelPrompt

A class that allows us to inline LM prompt strings without them being hard to read. Purely for formatting purposes.

#### __new__

```python
__new__(cls: Any, value: str)
```

### Function: parse_stimuli

```python
parse_stimuli(xml_string: str) -> tuple[(list[dict], list[dict])]
```

Parse XML string containing positive and negative stimuli and return them as dictionaries.

Args:
    xml_string (str): Input XML string containing stimuli

Returns:
    Dict with 'positive' and 'negative' keys containing lists of parsed conversations

### Function: claude_prompt

*Async function*

```python
claude_prompt(specification: str) -> tuple[(list[list[dict]], list[list[dict]])]
```

### Function: AsyncAutoEdits

*Async function*

```python
AsyncAutoEdits(specification: str, client: AsyncClient, model: SUPPORTED_MODELS, num_features_to_use: int)
```

### Function: AutoEdits

```python
AutoEdits(specification: str, client: Client, model: SUPPORTED_MODELS, num_features_to_use: int)
```

## goodfire/utils/logger.py

## goodfire/utils/conditional.py

### Class: Claude

#### __init__

```python
__init__(self: Any, anthropic_api_key: str, model_name: str, backup_models: Optional[list[str]])
```

#### chat

*Async method*

```python
chat(self: Any, message_history: Any, system_prompt: Optional[str], max_tokens_to_sample: int, temperature: float, max_retries: int)
```

### Class: LanguageModelPrompt

A class that allows us to inline LM prompt strings without them being hard to read. Purely for formatting purposes.

#### __new__

```python
__new__(cls: Any, value: str)
```

### Function: parse_stimuli

```python
parse_stimuli(xml_string: str) -> tuple[(list[dict], list[dict])]
```

Parse XML string containing positive and negative stimuli and return them as dictionaries.

Args:
    xml_string (str): Input XML string containing stimuli

Returns:
    Dict with 'positive' and 'negative' keys containing lists of parsed conversations

### Function: claude_prompt

*Async function*

```python
claude_prompt(specification: str) -> tuple[(list[list[dict]], list[list[dict]])]
```

### Function: AsyncAutoConditional

*Async function*

```python
AsyncAutoConditional(specification: str, client: AsyncClient, model: SUPPORTED_MODELS, num_features_to_use: int)
```

### Function: AutoConditional

```python
AutoConditional(specification: str, client: Client, model: Union[(Variant, SUPPORTED_MODELS)], num_features_to_use: int) -> ConditionalGroup
```

## goodfire/controller/interfaces.py

## goodfire/controller/controller.py

### Class: Intervention

#### json

```python
json(self: Any, scale: float) -> dict[(str, Any)]
```

#### from_json

```python
from_json(data: dict[(str, Any)]) -> Intervention
```

#### _prepare_values_for_stringification

```python
_prepare_values_for_stringification(self: Any)
```

#### __repr__

```python
__repr__(self: Any)
```

#### __str__

```python
__str__(self: Any)
```

#### as_code

```python
as_code(self: Any)
```

### Class: InterventionBuffer

#### __init__

```python
__init__(self: Any, controller: Controller)
```

#### __str__

```python
__str__(self: Any)
```

#### __repr__

```python
__repr__(self: Any)
```

#### pop

```python
pop(self: Any, index: int)
```

#### __getitem__

```python
__getitem__(self: Any, index: int)
```

#### __len__

```python
__len__(self: Any)
```

#### __iter__

```python
__iter__(self: Any)
```

#### __contains__

```python
__contains__(self: Any, intervention: Intervention)
```

#### push

```python
push(self: Any, intervention: Intervention)
```

#### insert

```python
insert(self: Any, intervention: Intervention, index: int)
```

#### empty

```python
empty(self: Any)
```

### Class: Scope

#### json

```python
json(self: Any, scale: float) -> dict[(str, Any)]
```

#### from_json

```python
from_json(data: dict[(str, Any)]) -> Scope
```

#### interrupt

```python
interrupt(self: Any, event_name: str)
```

### Class: Controller

#### __init__

```python
__init__(self: Any, _parent_controller: Optional[Controller])
```

#### buffer

```python
buffer(self: Any)
```

#### json

```python
json(self: Any, scale: float) -> dict[(str, Any)]
```

#### __str__

```python
__str__(self: Any)
```

#### __repr__

```python
__repr__(self: Any)
```

#### from_json

```python
from_json(data: dict[(str, Any)], name: Optional[str], id: Optional[str], _controller_cls: Optional[Type[Controller]]) -> Controller
```

#### when

```python
when(self: Any, conditional: Union[(Conditional, ConditionalGroup)])
```

#### __setitem__

```python
__setitem__(self: Any, key: Union[(Feature, FeatureGroup)], value: Union[(float, int, bool, InterventionProxy)])
```

#### __getitem__

```python
__getitem__(self: Any, key: Union[(Feature, FeatureGroup)]) -> InterventionProxy
```

#### _add_intervention

```python
_add_intervention(self: Any, features: FeatureGroup, value: float, mode: INTERVENTION_MODE)
```

#### __eq__

```python
__eq__(self: Any, other: Any)
```

### Class: InterventionProxy

#### __init__

```python
__init__(self: Any, controller: Controller, features: FeatureGroup)
```

#### __iadd__

```python
__iadd__(self: Any, value: float) -> InterventionProxy
```

#### __isub__

```python
__isub__(self: Any, value: float) -> InterventionProxy
```

#### __imul__

```python
__imul__(self: Any, value: float) -> InterventionProxy
```

#### __truediv__

```python
__truediv__(self: Any, value: float) -> InterventionProxy
```

### Class: ScopedController

#### from_json

```python
from_json(data: dict[(str, Any)]) -> ScopedController
```

## goodfire/controller/__init__.py

## goodfire/api/client.py

### Class: AsyncClient

Asyncio compatible client for interacting with the Goodfire API.

Attributes:
    features (FeaturesAPI): Interface for features operations
    chat (ChatAPI): Interface for chat operations
    variants (VariantsAPI): Interface for variants operations

#### __init__

```python
__init__(self: Any, api_key: str, base_url: str)
```

Initialize the client with an API key and base URL.

### Class: Client

Client for interacting with the Goodfire API.

Attributes:
    features (FeaturesAPI): Interface for features operations
    chat (ChatAPI): Interface for chat operations
    variants (VariantsAPI): Interface for variants operations

#### __init__

```python
__init__(self: Any, api_key: str, base_url: str)
```

Initialize the client with an API key and base URL.

## goodfire/api/constants.py

## goodfire/api/__init__.py

## goodfire/api/utils.py

### Class: HTTPWrapper

#### __init__

```python
__init__(self: Any, inital_backoff_time: float, max_retries: int)
```

#### get

```python
get(self: Any, url: str, headers: Optional[dict[(str, Any)]], params: Optional[dict[(str, Any)]], timeout: Optional[int]) -> Any
```

#### post

```python
post(self: Any, url: str, headers: Optional[dict[(str, Any)]], json: Optional[dict[(str, Any)]], timeout: Optional[int]) -> Any
```

#### put

```python
put(self: Any, url: str, headers: Optional[dict[(str, Any)]], json: Optional[dict[(str, Any)]], timeout: Optional[int]) -> Any
```

#### delete

```python
delete(self: Any, url: str, headers: Optional[dict[(str, Any)]], timeout: Optional[int]) -> Any
```

#### stream

```python
stream(self: Any, method: str, url: str, headers: Optional[dict[(str, Any)]], json: Optional[dict[(str, Any)]], params: Optional[dict[(str, Any)]], timeout: Optional[int], _attempt_num: int) -> Iterator[bytes]
```

### Class: AsyncHTTPWrapper

#### __init__

```python
__init__(self: Any, inital_backoff_time: float, max_retries: int)
```

#### _rate_limit_warning

```python
_rate_limit_warning(self: Any)
```

#### get

*Async method*

```python
get(self: Any, url: str, headers: Optional[dict[(str, Any)]], params: Optional[dict[(str, Any)]], _attempt_num: int, timeout: Optional[int]) -> Any
```

#### post

*Async method*

```python
post(self: Any, url: str, headers: Optional[dict[(str, Any)]], json: Optional[dict[(str, Any)]], _attempt_num: int, timeout: Optional[int]) -> Any
```

#### put

*Async method*

```python
put(self: Any, url: str, headers: Optional[dict[(str, Any)]], json: Optional[dict[(str, Any)]], _attempt_num: int, timeout: Optional[int]) -> Any
```

#### delete

*Async method*

```python
delete(self: Any, url: str, headers: Optional[dict[(str, Any)]], _attempt_num: int, timeout: Optional[int]) -> Any
```

#### stream

*Async method*

```python
stream(self: Any, method: str, url: str, headers: Optional[dict[(str, Any)]], json: Optional[dict[(str, Any)]], params: Optional[dict[(str, Any)]], timeout: Optional[int], _attempt_num: int) -> AsyncIterator[bytes]
```

## goodfire/api/exceptions.py

### Class: GoodfireBaseException

### Class: RateLimitException

### Class: InvalidRequestException

### Class: ForbiddenException

### Class: NotFoundException

### Class: UnauthorizedException

### Class: ServerErrorException

### Class: RequestFailedException

### Class: InsufficientFundsException

### Function: check_status_code

```python
check_status_code(status_code: int, respone_text: str)
```

## goodfire/api/chat/interfaces.py

### Class: StreamingDelta

### Class: StreamingChoice

### Class: StreamingChatCompletionChunk

### Class: ChatMessage

### Class: ChatCompletionChoice

### Class: ChatCompletion

### Class: LogitsResponse

## goodfire/api/chat/client.py

### Class: AsyncChatAPICompletions

OpenAI compatible chat completions API.

#### __init__

```python
__init__(self: Any, api_key: str, base_url: str)
```

#### _get_headers

```python
_get_headers(self: Any)
```

#### create

*Async method*

```python
create(self: Any, messages: Iterable[Union[(ChatMessage, dict[(str, str)])]], model: Union[(SUPPORTED_MODELS, Variant)], stream: bool, max_completion_tokens: Optional[int], top_p: float, temperature: float, stop: Optional[Union[(str, list[str])]], timeout: Optional[int], seed: Optional[int], system_prompt: str, _disable_moderation: bool) -> Union[(ChatCompletion, AsyncIterator[StreamingChatCompletionChunk])]
```

Create a chat completion.

### Class: AsyncChatAPI

OpenAI compatible chat API.

Example:
    >>> async for token in client.chat.completions.create(
    ...     [
    ...         {"role": "user", "content": "hello"}
    ...     ],
    ...     model="meta-llama/Meta-Llama-3.1-8B-Instruct",
    ...     stream=True,
    ...     max_completion_tokens=50,
    ... ):
    ...     print(token.choices[0].delta.content, end="")

#### __init__

```python
__init__(self: Any, api_key: str, base_url: str)
```

#### logits

*Async method*

```python
logits(self: Any, messages: Iterable[Union[(ChatMessage, dict[(str, str)])]], model: Union[(SUPPORTED_MODELS, Variant)], top_k: Optional[int], filter_vocabulary: Optional[list[str]]) -> LogitsResponse
```

Compute logits for a chat completion.

#### _get_headers

```python
_get_headers(self: Any)
```

### Class: ChatAPICompletions

#### __init__

```python
__init__(self: Any, api_key: str, base_url: str)
```

#### _get_headers

```python
_get_headers(self: Any)
```

#### create

```python
create(self: Any, messages: Iterable[Union[(ChatMessage, dict[(str, str)])]], model: Union[(SUPPORTED_MODELS, Variant)], stream: bool, max_completion_tokens: Optional[int], top_p: float, temperature: float, stop: Optional[Union[(str, list[str])]], timeout: Optional[int], seed: Optional[int], system_prompt: str, _disable_moderation: bool) -> Union[(ChatCompletion, Iterable[StreamingChatCompletionChunk])]
```

Create a chat completion.

### Class: ChatAPI

#### __init__

```python
__init__(self: Any, api_key: str, base_url: str)
```

#### logits

```python
logits(self: Any, messages: Iterable[Union[(ChatMessage, dict[(str, str)])]], model: Union[(SUPPORTED_MODELS, Variant)], top_k: Optional[int], filter_vocabulary: Optional[list[str]]) -> LogitsResponse
```

Compute logits for a chat completion.

## goodfire/api/chat/__init__.py

## goodfire/api/features/interfaces.py

### Class: FeatureResponse

Response object for a feature.

### Class: SearchFeatureResponseItem

Response object for a feature with relevance score.

### Class: SearchFeatureResponse

Response object for a list of features.

### Class: FeatureDetailsResponse

Response object for a feature with additional details.

### Class: ClusteringConfig

## goodfire/api/features/client.py

### Class: AsyncFeaturesAPI

A class for accessing interpretable SAE features of AI models.

#### __init__

```python
__init__(self: Any, goodfire_api_key: str, base_url: str)
```

#### _get_headers

```python
_get_headers(self: Any)
```

#### neighbors

*Async method*

```python
neighbors(self: Any, features: Union[(Feature, FeatureGroup)], model: Union[(SUPPORTED_MODELS, Variant)], top_k: int) -> FeatureGroup
```

Get the nearest neighbors of a feature or group of features.

#### search

*Async method*

```python
search(self: Any, query: str, model: Union[(SUPPORTED_MODELS, Variant)], top_k: int) -> FeatureGroup
```

Search for features based on a query.

#### semantic_similarity

*Async method*

```python
semantic_similarity(self: Any, features: FeatureGroup, query: str, model: Union[(SUPPORTED_MODELS, Variant)]) -> list[float]
```

#### rerank

*Async method*

```python
rerank(self: Any, features: FeatureGroup, query: str, model: Union[(SUPPORTED_MODELS, Variant)], top_k: int) -> FeatureGroup
```

Rerank a set of features based on a query.

#### activations

*Async method*

```python
activations(self: Any, messages: list[ChatMessage], model: Union[(SUPPORTED_MODELS, Variant)], features: Optional[Union[(Feature, FeatureGroup)]]) -> NDArray[Any]
```

Retrieve feature activations matrix for a set of messages.

#### inspect

*Async method*

```python
inspect(self: Any, messages: list[ChatMessage], model: Union[(SUPPORTED_MODELS, Variant)], features: Optional[Union[(Feature, FeatureGroup)]], aggregate_by: Literal[(frequency, mean, max, sum)], _fetch_feature_data: bool)
```

Inspect feature activations for a set of messages.

#### _tokenize

*Async method*

```python
_tokenize(self: Any, messages: list[ChatMessage], model: Union[(SUPPORTED_MODELS, Variant)])
```

Tokenize messages.

#### attribute

*Async method*

```python
attribute(self: Any, messages: list[ChatMessage], model: Union[(SUPPORTED_MODELS, Variant)])
```

#### steer_to_token

*Async method*

```python
steer_to_token(self: Any, messages: list[ChatMessage], model: Union[(SUPPORTED_MODELS, Variant)], steer_to: str)
```

#### contrast

*Async method*

```python
contrast(self: Any, dataset_1: list[list[ChatMessage]], dataset_2: list[list[ChatMessage]], model: Union[(SUPPORTED_MODELS, Variant)], top_k: int) -> tuple[(FeatureGroup, FeatureGroup)]
```

Identify features that differentiate between two conversation datasets.

Args:
    dataset_1: First conversation dataset
    dataset_2: Second conversation dataset
    model: Model identifier or variant interface
    top_k: Number of top features to return (default: 5)

Returns:
    tuple: Two FeatureGroups containing:
        - Features steering towards dataset_1
        - Features steering towards dataset_2

    Each Feature has properties:
        - uuid: Unique feature identifier
        - label: Human-readable feature description
        - max_activation_strength: Feature activation strength
        - index_in_sae: Index in sparse autoencoder

Raises:
    ValueError: If datasets are empty or have different lengths

Example:
    >>> dataset_1 = [[
    ...     {"role": "user", "content": "Hi how are you?"},
    ...     {"role": "assistant", "content": "I'm doing well..."}
    ... ]]
    >>> dataset_2 = [[
    ...     {"role": "user", "content": "Hi how are you?"},
    ...     {"role": "assistant", "content": "Arr my spirits be high..."}
    ... ]]
    >>> features_1, features_2 = client.features.contrast(
    ...     dataset_1=dataset_1,
    ...     dataset_2=dataset_2,
    ...     model=model,
    ...     dataset_2_feature_rerank_query="pirate",
    ...     top_k=5
    ... )

#### lookup

*Async method*

```python
lookup(self: Any, indices: list[int], model: Union[(SUPPORTED_MODELS, Variant)]) -> dict[(int, Feature)]
```

#### generate_contrastive_stimulus

*Async method*

```python
generate_contrastive_stimulus(self: Any, specification: str)
```

#### _list

*Async method*

```python
_list(self: Any, ids: list[str]) -> FeatureGroup
```

Get features by their IDs.

### Class: FeatureActivation

#### __init__

```python
__init__(self: Any, feature: Feature, activation_strength: float)
```

#### __repr__

```python
__repr__(self: Any)
```

#### __str__

```python
__str__(self: Any)
```

### Class: FeatureActivations

#### __init__

```python
__init__(self: Any, acts: Iterable[tuple[(Feature, float)]], model: Union[(SUPPORTED_MODELS, Variant)])
```

#### __getitem__

```python
__getitem__(self: Any, idx: int)
```

#### __iter__

```python
__iter__(self: Any)
```

#### __len__

```python
__len__(self: Any)
```

#### __repr__

```python
__repr__(self: Any)
```

#### __str__

```python
__str__(self: Any)
```

#### vector

```python
vector(self: Any)
```

#### lookup

```python
lookup(self: Any) -> dict[(int, Feature)]
```

### Class: Token

#### __init__

```python
__init__(self: Any, context: ContextInspector, token: str, feature_acts: list[dict[(str, Any)]])
```

#### __repr__

```python
__repr__(self: Any)
```

#### __str__

```python
__str__(self: Any)
```

#### inspect

```python
inspect(self: Any, k: int)
```

#### vector

```python
vector(self: Any) -> NDArray[Any]
```

#### lookup

```python
lookup(self: Any) -> dict[(int, Feature)]
```

### Class: ContextInspector

#### __init__

```python
__init__(self: Any, client: AsyncFeaturesAPI, context_response: dict[(str, Any)], model: Union[(SUPPORTED_MODELS, Variant)], aggregate_by: Literal[(frequency, mean, max, sum)], include_feature_ids: Optional[set[str]])
```

#### fetch_features

*Async method*

```python
fetch_features(self: Any)
```

#### __repr__

```python
__repr__(self: Any)
```

#### __str__

```python
__str__(self: Any)
```

#### top

```python
top(self: Any, k: int)
```

#### matrix

```python
matrix(self: Any)
```

#### lookup

```python
lookup(self: Any) -> dict[(int, Feature)]
```

### Class: FeaturesAPI

#### __init__

```python
__init__(self: Any, api_key: str, base_url: str)
```

#### neighbors

```python
neighbors(self: Any, features: Union[(Feature, FeatureGroup)], model: Union[(SUPPORTED_MODELS, Variant)], top_k: int) -> FeatureGroup
```

#### search

```python
search(self: Any, query: str, model: Union[(SUPPORTED_MODELS, Variant)], top_k: int) -> FeatureGroup
```

#### rerank

```python
rerank(self: Any, features: FeatureGroup, query: str, model: Union[(SUPPORTED_MODELS, Variant)], top_k: int) -> FeatureGroup
```

#### activations

```python
activations(self: Any, messages: list[ChatMessage], model: Union[(SUPPORTED_MODELS, Variant)], features: Optional[Union[(Feature, FeatureGroup)]]) -> NDArray[Any]
```

#### inspect

```python
inspect(self: Any, messages: list[ChatMessage], model: Union[(SUPPORTED_MODELS, Variant)], features: Optional[Union[(Feature, FeatureGroup)]], aggregate_by: Literal[(frequency, mean, max, sum)], _fetch_feature_data: bool)
```

#### contrast

```python
contrast(self: Any, dataset_1: list[list[ChatMessage]], dataset_2: list[list[ChatMessage]], model: Union[(SUPPORTED_MODELS, Variant)], top_k: int) -> tuple[(FeatureGroup, FeatureGroup)]
```

#### lookup

```python
lookup(self: Any, indices: list[int], model: Union[(SUPPORTED_MODELS, Variant)]) -> dict[(int, Feature)]
```

#### attribution

```python
attribution(self: Any, prefix: list[ChatMessage], model: Union[(SUPPORTED_MODELS, Variant)], steer_to: str, steer_away: str)
```

#### generate_contrastive_stimulus

```python
generate_contrastive_stimulus(self: Any, specification: str)
```

#### attribute

```python
attribute(self: Any, messages: list[ChatMessage], model: Union[(SUPPORTED_MODELS, Variant)])
```

#### steer_to_token

```python
steer_to_token(self: Any, messages: list[ChatMessage], model: Union[(SUPPORTED_MODELS, Variant)], steer_to: str)
```

## goodfire/api/features/__init__.py

